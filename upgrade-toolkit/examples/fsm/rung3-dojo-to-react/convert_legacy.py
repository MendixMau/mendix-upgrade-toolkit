#!/usr/bin/env python3
"""Generate an mxcli MDL script that replaces legacy (Dojo-only) widgets with
React-ready pluggable ones, reading a `mx dump-mpr` JSON.

usage: convert_legacy.py DUMP.json OUT.mdl [--module M] [--gaps gaps.json] [--only Unit.Name]

Deterministic: units sorted by qualified name, widgets in document order.
Every replacement is its own ALTER statement so exec --continue-on-error can
isolate a bad widget.
"""
import json, sys, re, collections, argparse

LEGACY = {
    'Pages$DataGrid': 'DataGrid', 'Pages$ReferenceSelector': 'ReferenceSelector',
    'Pages$InputReferenceSetSelector': 'InputReferenceSetSelector',
    'Pages$ReferenceSetSelector': 'ReferenceSetSelector', 'Pages$DropDown': 'DropDown',
    'Pages$StaticImageViewer': 'StaticImageViewer', 'Pages$DynamicImageViewer': 'DynamicImageViewer',
    'Pages$TemplateGrid': 'TemplateGrid',
}
UNIT_KINDS = {'Pages$Page': 'PAGE', 'Pages$Snippet': 'SNIPPET', 'Pages$Layout': 'LAYOUT'}

# ---------------------------------------------------------------- model index
class Model:
    def __init__(self, d):
        self.units = d['units']
        self.byq = {}
        self.ent_gen = {}          # entity -> parent entity
        self.attr = {}             # qualified attr -> attribute type dict
        self.mf_params = {}        # microflow/nanoflow qname -> [(name, kind, entity)]
        self.page_params = {}      # page/snippet qname -> [(name, entity)]
        self.ent_by_id = {}
        self.assoc = {}            # association qname -> (parent, child, type, owner)
        for u in self.units:
            q = u.get('$QualifiedName')
            if q: self.byq[q] = u
            t = u['$Type']
            if t == 'DomainModels$DomainModel':
                for e in u['entities']:
                    self.ent_by_id[e['$ID']] = e['$QualifiedName']
                    g = e.get('generalization') or {}
                    if g.get('$Type') == 'DomainModels$Generalization':
                        self.ent_gen[e['$QualifiedName']] = g['generalization']
                    for a in e['attributes']:
                        self.attr[a['$QualifiedName']] = a['type']
            elif t in ('Microflows$Microflow', 'Microflows$Nanoflow'):
                ps = []
                for o in u['objectCollection']['objects']:
                    if o['$Type'] == 'Microflows$MicroflowParameterObject':
                        vt = o['variableType']
                        ps.append((o['name'], 'list' if vt['$Type'] == 'DataTypes$ListType' else
                                   'object' if vt['$Type'] == 'DataTypes$ObjectType' else 'prim', vt.get('entity')))
                    elif o['$Type'] == 'Microflows$NanoflowParameterObject' or 'Parameter' in o['$Type']:
                        vt = o.get('variableType') or {}
                        ps.append((o['name'], 'list' if vt.get('$Type') == 'DataTypes$ListType' else
                                   'object' if vt.get('$Type') == 'DataTypes$ObjectType' else 'prim', vt.get('entity')))
                self.mf_params[q] = ps
            elif t in ('Pages$Page', 'Pages$Snippet'):
                self.page_params[q] = [(p['name'], (p.get('parameterType') or {}).get('entity'))
                                       for p in u.get('parameters', [])]

    def build_assoc(self):
        for u in self.units:
            if u['$Type'] == 'DomainModels$DomainModel':
                for a in u.get('associations', []) + u.get('crossAssociations', []):
                    par = self.ent_by_id.get(a['parent'], a['parent'])
                    chi = self.ent_by_id.get(a['child'], a['child'])
                    self.assoc[a['$QualifiedName']] = (par, chi, a.get('type'), a.get('owner'))

    def nav_ok(self, src_ent, assoc):
        """can an attribute path leave src_ent through assoc? (parent side always, child side only for owner Both)"""
        a = self.assoc.get(assoc)
        if a is None or not src_ent: return True
        par, chi, ty, owner = a
        if self.is_a(src_ent, par): return True
        if self.is_a(src_ent, chi) and owner == 'Both': return True
        return False

    def path_nav_ok(self, ref, base_ent):
        er = ref.get('entityRef') if ref else None
        if not er or er['$Type'] != 'DomainModels$IndirectEntityRef': return True
        cur = base_ent
        for st in er['steps']:
            if not self.nav_ok(cur, st['association']): return False
            cur = st['destinationEntity']
        return True

    def is_a(self, ent, want):
        while ent:
            if ent == want: return True
            ent = self.ent_gen.get(ent)
        return False


def find(o, t):
    if isinstance(o, dict):
        if o.get('$Type') == t: yield o
        for v in o.values(): yield from find(v, t)
    elif isinstance(o, list):
        for v in o: yield from find(v, t)


def txt(t, lang='en_US'):
    if not t: return ''
    if t.get('$Type') == 'Pages$ClientTemplate':
        return txt(t.get('template'), lang)
    ts = t.get('translations', [])
    for x in ts:
        if x['languageCode'] == lang and x['text']: return x['text']
    for x in ts:
        if x['text']: return x['text']
    return ''


def q(s):
    return "'" + str(s).replace("'", "''").replace('\r', ' ').replace('\n', ' ') + "'"


def xp(s):
    return re.sub(r'\s+', ' ', s).strip()


def mod(qn): return qn.split('.')[0]


# --------------------------------------------------------------- the converter
class Conv:
    def __init__(self, M):
        self.M = M
        self.counts = collections.Counter()
        self.gaps = []             # dicts
        self.notes = collections.Counter()
        self.buttons = collections.Counter()   # control bar item -> outcome

    # ------------------------------------------------------------ bookkeeping
    def gap(self, unit, widget, reason):
        self.gaps.append({'unit': unit, 'widget': widget, 'reason': reason})

    # ----------------------------------------------------------- expressions
    def var(self, v):
        if not v: return None
        for k in ('pageParameter', 'snippetParameter', 'localVariable', 'widget'):
            if v.get(k): return '$' + v[k]
        return None

    def path(self, ref, with_attr=True, base_attr=None):
        """AttributeRef -> 'Mod.Assoc/Mod.Assoc2/Attr'"""
        steps = []
        er = ref.get('entityRef') if ref else None
        if er and er['$Type'] == 'DomainModels$IndirectEntityRef':
            steps = [s['association'] for s in er['steps']]
        attr = ref['attribute'].split('.')[-1] if ref else None
        parts = list(steps) + ([attr] if with_attr and attr else [])
        return '/'.join(parts)

    def dest_entity(self, ref):
        er = ref.get('entityRef') if ref else None
        if er and er['$Type'] == 'DomainModels$IndirectEntityRef':
            return er['steps'][-1]['destinationEntity']
        if er and er['$Type'] == 'DomainModels$DirectEntityRef':
            return er['entity']
        return ref['attribute'].rsplit('.', 1)[0] if ref else None

    def attr_kind(self, qattr):
        t = self.M.attr.get(qattr)
        if not t: return None, None
        ty = t['$Type'].split('$')[1].replace('AttributeType', '')
        return ty, t.get('enumeration')

    # --------------------------------------------------------------- context
    def ctx_lookup(self, ctx, entity):
        for e, expr in reversed(ctx):
            if e and entity and self.M.is_a(e, entity):
                return expr
        return None

    def args_for(self, params, mappings, ctx, unit, wname, selmap=None, list_sel=None):
        """Build `P = expr` list for a flow/page call. selmap: widget name -> expression."""
        mapped = {}
        for m in mappings:
            pname = m['parameter'].split('.')[-1]
            v = m.get('variable')
            expr = None
            if m.get('expression') or m.get('argument'):
                expr = xp(m.get('expression') or m.get('argument'))
            elif v:
                w = v.get('widget')
                if w and selmap and w in selmap:
                    expr = selmap[w]
                else:
                    expr = self.var(v)
                    if v.get('subKey'): expr = None
            mapped[pname] = expr
        out = []
        for (pn, kind, ent) in params:
            if pn in mapped:
                if mapped[pn] is None:
                    self.gap(unit, wname, 'argument %s: unsupported variable mapping' % pn)
                    return None
                out.append('%s = %s' % (pn, mapped[pn]))
            elif kind == 'object':
                e = self.ctx_lookup(ctx, ent)
                if e is None and (self.M.byq.get(unit) or {}).get('$Type') == 'Pages$Snippet':
                    e = '$currentObject'
                    self.notes['snippet argument %s taken from caller context ($currentObject)' % pn] += 1
                if e is None:
                    self.gap(unit, wname, 'argument %s (%s): no enclosing context object found' % (pn, ent))
                    return None
                out.append('%s = %s' % (pn, e))
            elif kind == 'list':
                self.gap(unit, wname, 'argument %s: list parameter without mapping' % pn)
                return None
        return out

    # ---------------------------------------------------------------- actions
    def settings_clause(self, s, dis_default_true=True, disabled=None, flow=True):
        parts = []
        if disabled is not None and disabled != dis_default_true:
            parts.append('DisabledDuringExecution: %s' % ('true' if disabled else 'false'))
        if flow:
            pb = s.get('progressBar')
            if pb and pb != 'None': parts.append('ProgressBar: %s' % pb)
            pm = txt(s.get('progressMessage'))
            if pm: parts.append('ProgressMessage: %s' % q(pm))
            ci = s.get('confirmationInfo')
            if ci:
                parts.append('Confirmation: %s' % q(txt(ci['question'])))
                pc, cc = txt(ci['proceedButtonCaption']), txt(ci['cancelButtonCaption'])
                if pc and pc != 'Proceed': parts.append('ProceedCaption: %s' % q(pc))
                if cc and cc != 'Cancel': parts.append('CancelCaption: %s' % q(cc))
            if s.get('formValidations') and s['formValidations'] != 'All':
                parts.append('FormValidations: %s' % s['formValidations'])
        return parts

    def action(self, a, ctx, unit, wname, selmap=None):
        """-> MDL action text or None (None = no action) ; raises KeyError-free; returns '' on gap"""
        if not a: return None
        t = a['$Type']
        dis = a.get('disabledDuringExecution')
        if t == 'Pages$NoClientAction': return None
        if t == 'Pages$MicroflowClientAction':
            s = a['microflowSettings']; mf = s['microflow']
            params = self.M.mf_params.get(mf)
            if params is None:
                self.gap(unit, wname, 'microflow %s not found in dump' % mf); return ''
            args = self.args_for(params, s['parameterMappings'], ctx, unit, wname, selmap)
            if args is None: return ''
            st = self.settings_clause(s, disabled=dis)
            if s.get('asynchronous'): st.append('Asynchronous: true')
            txtv = 'CALL MICROFLOW %s(%s)' % (mf, ', '.join(args))
            if st: txtv += ' with (%s)' % ', '.join(st)
            return txtv
        if t == 'Pages$CallNanoflowClientAction':
            mf = a['nanoflow']
            params = self.M.mf_params.get(mf)
            if params is None:
                self.gap(unit, wname, 'nanoflow %s not found in dump' % mf); return ''
            args = self.args_for(params, a['parameterMappings'], ctx, unit, wname, selmap)
            if args is None: return ''
            st = self.settings_clause(a, disabled=dis)
            txtv = 'CALL NANOFLOW %s(%s)' % (mf, ', '.join(args))
            if st: txtv += ' with (%s)' % ', '.join(st)
            return txtv
        if t == 'Pages$PageClientAction':
            s = a['pageSettings']; pg = s['page']
            if not pg:
                self.gap(unit, wname, 'show page action without page'); return ''
            if a.get('pagesForSpecializations'):
                self.gap(unit, wname, 'show page: page-for-specialization settings dropped');
            if s.get('titleOverride') and txt(s['titleOverride']):
                self.gap(unit, wname, 'show page: title override dropped')
            params = [(n, 'object', e) for (n, e) in self.M.page_params.get(pg, [])]
            args = self.args_for(params, s['parameterMappings'], ctx, unit, wname, selmap)
            if args is None: return ''
            txtv = 'SHOW PAGE %s(%s)' % (pg, ', '.join(args))
            if dis is False: txtv += ' with (DisabledDuringExecution: false)'
            return txtv
        if t == 'Pages$DeleteClientAction':
            return 'DELETE CLOSE PAGE' if a.get('closePage') else 'DELETE'
        if t == 'Pages$SaveChangesClientAction':
            return 'SAVE CHANGES CLOSE PAGE' if a.get('closePage') else 'SAVE CHANGES'
        if t == 'Pages$CancelChangesClientAction':
            return 'CANCEL CHANGES CLOSE PAGE' if a.get('closePage') else 'CANCEL CHANGES'
        if t == 'Pages$ClosePageClientAction':
            return 'CLOSE PAGE'
        self.gap(unit, wname, 'unsupported action type %s' % t)
        return ''

    # ----------------------------------------------------------- common props
    def common(self, w, unit, ctx=None, classes=True, target='widget'):
        widget_is_image = toggle_ok = False
        p = []
        ap = w.get('appearance') or {}
        if classes:
            if ap.get('class'): p.append('Class: %s' % q(ap['class']))
            if ap.get('style'): p.append('Style: %s' % q(ap['style']))
            if ap.get('dynamicClasses'): p.append('DynamicClasses: %s' % q(xp(ap['dynamicClasses'])))
            dps = []
            spacing = []
            sz = {'Smaller': 'XS', 'Small': 'S', 'Medium': 'M', 'Large': 'L', 'Larger': 'XL', 'S': 'S', 'M': 'M', 'L': 'L', 'XS': 'XS', 'XL': 'XL'}
            for dp in ap.get('designProperties', []):
                v = dp['value']; k = dp['key']
                if k.startswith('Spacing') or k.startswith('Padding'):
                    kind_ = 'margin' if k.startswith('Spacing') else 'padding'
                    sides = [k.split(' ', 1)[1].lower()] if ' ' in k else []
                    if v['$Type'] == 'Pages$OptionDesignPropertyValue' and sides:
                        o = sz.get(v['option'])
                        if o: spacing.append("'%s-%s': '%s'" % (kind_, sides[0], o))
                        elif v['option'] != 'None': self.notes['design property %s=%s dropped' % (k, v['option'])] += 1
                    elif v['$Type'] == 'Pages$CompoundDesignPropertyValue':
                        for sp in v['properties']:
                            o = sz.get(sp['value'].get('option'))
                            if o: spacing.append("'%s': '%s'" % (sp['key'], o))
                    continue
                if k == 'Spacing' and v['$Type'] == 'Pages$CompoundDesignPropertyValue':
                    for sp in v['properties']:
                        o = sz.get(sp['value'].get('option'))
                        if o: spacing.append("'%s': '%s'" % (sp['key'], o))
                    continue
                if not widget_is_image and not toggle_ok:
                    pass
                self.notes['design property dropped (not defined on %s): %s' % (target, k)] += 1
            if spacing: dps.append("'Spacing': (%s)" % ', '.join(spacing))
            if dps: p.append('DesignProperties: (%s)' % ', '.join(dps))
        cv = w.get('conditionalVisibilitySettings')
        if cv:
            e = self.visibility(cv, unit, w['name'])
            if e: p.append('Visible: %s' % q(e))
        ce = w.get('conditionalEditabilitySettings')
        if ce:
            self.gap(unit, w['name'], 'conditional editability not converted')
        return p

    def visibility(self, cv, unit, wname):
        if cv.get('moduleRoles'):
            self.gap(unit, wname, 'visibility by module role dropped')
        if cv.get('expression'):
            return xp(cv['expression'])
        if cv.get('attribute') and cv.get('conditions'):
            root = self.var(cv.get('sourceVariable')) or '$currentObject'
            attr = cv['attribute']
            ty, en = self.attr_kind(attr)
            ref = '%s/%s' % (root, attr.split('.')[-1])
            vis = [c['attributeValue'] for c in cv['conditions'] if c['editableVisible']]
            if ty == 'Boolean':
                if vis == ['true']: return ref
                if vis == ['false']: return 'not(%s)' % ref
                return 'true'
            if not vis: return 'false'
            terms = []
            for v in vis:
                if v == '(empty)': terms.append('%s = empty' % ref)
                elif en: terms.append('%s = %s.%s' % (ref, en, v))
                else:
                    self.gap(unit, wname, 'visibility condition on non-enum attribute %s' % attr); return None
            return ' or '.join(terms)
        return None

    def label(self, w, unit):
        lt = w.get('labelTemplate')
        if lt and lt.get('parameters'):
            self.gap(unit, w['name'], 'label has template parameters; static text used')
        return txt(lt) if lt else ''

    # widgets for which mxcli cannot resolve the enclosing data view's entity (bug M3):
    # write the context variable explicitly instead
    FORCE_VAR = {('NativeMobileTimeRegistration.NativeTimeRegistrationNP_NewEdit', 'referenceSelector1'),
                 ('NativeMobileTimeRegistration.NativeTimeRegistrationNP_NewEdit', 'referenceSelector2')}

    def in_attr(self, w, rel, unit=None, ctx=None):
        sv = self.var(w.get('sourceVariable'))
        if not sv and (unit, w['name']) in self.FORCE_VAR and ctx:
            sv = ctx[-1][1]
        return (sv + '.' + rel) if sv else rel

    # ------------------------------------------------------------ data sources
    def sort_clause(self, sortbar, base=None):
        items = []
        for si in (sortbar or {}).get('sortItems', []):
            if base and not self.M.path_nav_ok(si['attributeRef'], base):
                self.notes['sort item dropped (path against association owner)'] += 1; continue
            items.append('%s %s' % (self.path(si['attributeRef']), 'DESC' if si['sortDirection'] == 'Descending' else 'ASC'))
        return (' SORT BY ' + ', '.join(items)) if items else ''

    def flow_source(self, ms, ctx, unit, wname):
        mf = ms['microflow']
        params = self.M.mf_params.get(mf)
        if params is None:
            self.gap(unit, wname, 'datasource microflow %s not found' % mf); return None
        args = self.args_for(params, ms['parameterMappings'], ctx, unit, wname)
        if args is None: return None
        return 'MICROFLOW %s(%s)' % (mf, ', '.join(args))

    # ================================================================ widgets
    def conv_image(self, w, unit, kind, ctx):
        name = w['name']
        p = []
        if w['$Type'] == 'Pages$StaticImageViewer':
            p.append('Image: %s' % q(w['image'])) if w.get('image') else self.gap(unit, name, 'static image without image')
        else:
            ds = w['dataSource']
            ent = (ds.get('entityRef') or {}).get('entity')
            sv = self.var(ds.get('sourceVariable'))
            if w.get('defaultImage'): p.append('DefaultImage: %s' % q(w['defaultImage']))
            self.gap(unit, name, 'dynamic image (entity %s): IMAGE object binding not expressible in MDL' % ent)
            return None
        alt = txt(w.get('alternativeText'))
        if alt: p.append('AlternativeText: %s' % q(alt))
        for unitk, key in (('widthUnit', 'width'), ('heightUnit', 'height')):
            u = w.get(unitk)
            if u and u != 'Auto':
                p.append("%s: '%s'" % (unitk, u.lower()))
                p.append('%s: %s' % (key, w[key]))
        if w.get('showAsThumbnail'): p.append("displayAs: 'thumbnail'")
        ca = w.get('clickAction')
        if w.get('onClickEnlarge'):
            p.append("onClickType: 'enlarge'")
        elif ca and ca['$Type'] != 'Pages$NoClientAction':
            a = self.action(ca, ctx, unit, name)
            if a: p.append('OnClick: %s' % a)
        p += self.common(w, unit, ctx)
        return 'IMAGE %s (%s)' % (name, ', '.join(p))

    def conv_dropdown(self, w, unit, ctx):
        name = w['name']
        ref = w['attributeRef']
        p = []
        lbl = self.label(w, unit)
        if lbl: p.append('Label: %s' % q(lbl))
        p.append('Attribute: %s' % self.in_attr(w, ref['attribute'].split('.')[-1]))
        if w.get('editable') == 'Never': p.append('Editable: Never')
        eo = txt(w.get('emptyOptionCaption'))
        if eo: p.append('EmptyOptionText: %s' % q(eo))
        for key, mdl in (('onChangeAction', 'OnChange'), ('onEnterAction', 'OnEnter'), ('onLeaveAction', 'OnLeave')):
            a = self.action(w.get(key), ctx, unit, name)
            if a: p.append('%s: %s' % (mdl, a))
        p += self.common(w, unit, ctx)
        return 'COMBOBOX %s (%s)' % (name, ', '.join(p))

    def conv_refselector(self, w, unit, ctx, multi=False):
        name = w['name']
        ref = w['attributeRef']
        er = ref.get('entityRef')
        if not er or er['$Type'] != 'DomainModels$IndirectEntityRef':
            self.gap(unit, name, 'reference selector without association path'); return None
        assoc = er['steps'][-1]['association']
        if len(er['steps']) > 1:
            self.gap(unit, name, 'reference selector over multi-step path %s' % '/'.join(s['association'] for s in er['steps']))
            return None
        dest = er['steps'][-1]['destinationEntity']
        p = []
        lbl = self.label(w, unit)
        if lbl: p.append('Label: %s' % q(lbl))
        p.append('Attribute: %s' % self.in_attr(w, assoc, unit, ctx))
        cty, _ = self.attr_kind(ref['attribute'])
        if cty in (None, 'String'):
            p.append('CaptionAttribute: %s' % ref['attribute'].split('.')[-1])
        else:
            fn = 'getCaption' if cty == 'Enumeration' else 'toString'
            p.append("optionsSourceAssociationCaptionType: expression")
            p.append("optionsSourceAssociationCaptionExpression: %s" % q('%s($currentObject/%s)' % (fn, ref['attribute'].split('.')[-1])))
            self.notes['combo box caption of a non-string attribute written as %s() expression' % fn] += 1
        src = w.get('selectorSource') or {}
        if src.get('$Type') == 'Pages$SelectorMicroflowSource':
            s = self.flow_source(src['dataSourceMicroflowSettings'], ctx, unit, name)
            if s is None: return None
            p.append('DataSource: %s' % s)
        elif src.get('$Type') == 'Pages$SelectorXPathSource':
            xpc = xp(src.get('xPathConstraint') or '')
            srt = self.sort_clause(src.get('sortBar'), dest)
            if src.get('constrainedByRefs'):
                self.gap(unit, name, 'selector constrainedByRefs (dependent drop-down) dropped')
            p.append('DataSource: DATABASE %s%s%s' % (dest, (' WHERE ' + xpc) if xpc else '', srt))
        if w.get('editable') == 'Never': p.append('Editable: Never')
        eo = txt(w.get('emptyOptionCaption'))
        if eo: p.append('EmptyOptionText: %s' % q(eo))
        a = self.action(w.get('onChangeAction'), ctx, unit, name)
        if a: p.append('OnChange: %s' % a)
        if (w.get('gotoPageSettings') or {}).get('page'):
            self.gap(unit, name, 'selector go-to page dropped')
        sp = (w.get('selectPageSettings') or {}).get('page')
        if sp: self.notes['select page binding removed (CE9900)'] += 1
        p += self.common(w, unit, ctx)
        return 'COMBOBOX %s (%s)' % (name, ', '.join(p))

    # ------------------------------------------------------------- data grid
    def conv_grid(self, g, unit, ctx, used_names, kind):
        name = g['name']
        ds = g['dataSource']
        dst = ds['$Type']
        # ---- data source
        dsrc = None
        entity = None
        er = ds.get('entityRef')
        if er:
            entity = er['entity'] if er['$Type'] == 'DomainModels$DirectEntityRef' else er['steps'][-1]['destinationEntity']
        sv = self.var(ds.get('sourceVariable'))
        if dst == 'Pages$GridXPathSource':
            xpc = xp(ds.get('xPathConstraint') or '')
            srt = self.sort_clause(ds.get('sortBar'), entity)
            if er and er['$Type'] == 'DomainModels$IndirectEntityRef':
                if not sv:
                    sv = ctx[-1][1] if ctx else None
                if not sv:
                    self.gap(unit, name, 'XPath grid over association path without source variable'); return None
                chain = sv + '/' + '/'.join('%s/%s' % (s['association'], s['destinationEntity']) for s in er['steps'])
                if "'[%CurrentObject%]'" in xpc:
                    xpc = xpc.replace("'[%CurrentObject%]'", sv)
                    self.notes['[%CurrentObject%] replaced by the source variable in a DATABASE FROM xpath'] += 1
                dsrc = 'DATABASE FROM %s%s%s' % (chain, (' WHERE ' + xpc) if xpc else '', srt)
            elif er:
                dsrc = 'DATABASE %s%s%s' % (entity, (' WHERE ' + xpc) if xpc else '', srt)
            else:
                self.gap(unit, name, 'XPath grid without entity'); return None
        elif dst == 'Pages$AssociationSource' or dst == 'Pages$ReferenceSetSource':
            if not sv:
                sv = '$currentObject'
            chain = sv + '/' + '/'.join(s['association'] for s in er['steps'])
            dsrc = chain
        elif dst == 'Pages$MicroflowSource':
            s = self.flow_source(ds['microflowSettings'], ctx, unit, name)
            if s is None: return None
            dsrc = s
            # entity: microflow return type
            mf = self.M.byq.get(ds['microflowSettings']['microflow'])
            rt = (mf or {}).get('microflowReturnType') or {}
            entity = rt.get('entity')
        else:
            self.gap(unit, name, 'grid data source %s' % dst); return None

        gctx = ctx + [(entity, '$currentObject')]
        # ---- columns
        cols = []
        col_by_path = {}
        for c in g['columns']:
            ref = c.get('attributeRef')
            if ref is None:
                self.gap(unit, name, 'column %s without attribute' % txt(c['caption']))
                continue
            if c.get('editable'): self.gap(unit, name, 'inline-editable column %s' % txt(c['caption']))
            if c['formattingInfo']['enumFormat'] == 'Image':
                self.gap(unit, name, 'column %s: enumeration shown as image, text used' % (txt(c['caption']) or ref['attribute']))
            if not self.M.path_nav_ok(ref, entity):
                self.gap(unit, name, 'column %s dropped: attribute path %s runs against the association owner (not navigable in a data grid 2)' % (txt(c['caption']), self.path(ref)))
                continue
            pth = self.path(ref)
            cap = txt(c['caption'])
            props = ['Attribute: %s' % pth, 'Caption: %s' % q(cap)]
            if c.get('width'):
                props.append('ColumnWidth: manual'); props.append('Size: %s' % max(int(c['width']), 1))
            col = {'path': pth, 'props': props, 'filter': None, 'hidden': False, 'ref': ref}
            cols.append(col)
            col_by_path.setdefault(pth, col)

        # ---- search fields -> filters
        sbar = ds.get('searchBar') or {}
        extra = []
        for sf in sbar.get('items', []):
            ref = sf['attributeRef']
            if not self.M.path_nav_ok(ref, entity):
                self.gap(unit, name, 'search field %s dropped: attribute path %s runs against the association owner (no column filter possible)' % (sf['name'], self.path(ref)))
                continue
            pth = self.path(ref)
            ty, en = self.attr_kind(ref['attribute'])
            fname = sf['name']
            if fname in used_names: fname = '%s_%s' % (name, fname)
            used_names.add(fname)
            isref = bool(ref.get('entityRef'))
            op = sf.get('operator', 'Equal')
            dflt = sf.get('defaultValue') or ''
            fprops = []
            if sf['$Type'] == 'Pages$DropDownSearchField' or ty in ('Enumeration', 'Boolean'):
                if ty in ('Enumeration', 'Boolean') or (ty is None and not isref):
                    ftype = 'DROPDOWNFILTER'
                    if sf['$Type'] == 'Pages$DropDownSearchField' and sf.get('allowMultipleSelect'): fprops.append('multiSelect: true')
                    if dflt: fprops.append('defaultValue: %s' % q("'%s'" % dflt))
                else:
                    ftype = 'TEXTFILTER'
                    fprops.append("defaultFilter: 'equal'")
                    if dflt: fprops.append('defaultValue: %s' % q("'%s'" % dflt))
                    if isref: self.notes['association drop-down search field approximated by text filter'] += 1
                    if sf.get('xPathConstraint') or sf.get('allowMultipleSelect'):
                        self.gap(unit, name, 'search field %s: drop-down options XPath / multi-select approximated by a text filter' % fname)
            else:
                dfm = {'Contains': 'contains', 'Equal': 'equal', 'StartsWith': 'startsWith', 'EndsWith': 'endsWith',
                       'Greater': 'greater', 'GreaterOrEqual': 'greaterEqual', 'Less': 'smaller',
                       'LessOrEqual': 'smallerEqual', 'NotEqual': 'notEqual'}.get(op)
                if ty == 'String' or ty is None:
                    ftype = 'TEXTFILTER'
                    if dfm and dfm != 'contains': fprops.append("defaultFilter: '%s'" % dfm)
                    if dflt: fprops.append('defaultValue: %s' % q(q(dflt)))
                elif ty in ('Integer', 'Long', 'Decimal', 'AutoNumber'):
                    ftype = 'NUMBERFILTER'
                    if dfm and dfm != 'equal': fprops.append("defaultFilter: '%s'" % dfm)
                    if dflt: fprops.append('defaultValue: %s' % q(dflt))
                elif ty == 'DateTime':
                    ftype = 'DATEFILTER'
                    if dfm and dfm != 'equal': fprops.append("defaultFilter: '%s'" % dfm)
                else:
                    ftype = 'TEXTFILTER'
                    self.gap(unit, name, 'search field %s: attribute type %s filtered as text' % (fname, ty))
            flt = '%s %s%s' % (ftype, fname, (' (%s)' % ', '.join(fprops)) if fprops else '')
            col = col_by_path.get(pth)
            if col is None or col['filter'] is not None:
                # host the filter in an extra hidden column
                col = {'path': pth, 'props': ['Attribute: %s' % pth, 'Caption: %s' % q(txt(sf['caption']) or fname),
                                              'Hidable: hidden'], 'filter': None, 'hidden': True, 'ref': ref}
                cols.append(col)
                if pth not in col_by_path: col_by_path[pth] = col
                self.notes['search field without matching column: hidden host column added'] += 1
            else:
                col['props'][1] = col['props'][1]
            col['filter'] = flt
            self.notes['search field -> %s' % ftype] += 1

        # ---- control bar
        cb = g['controlBar']
        items = cb.get('items', [])
        default_id = cb.get('defaultButton')
        above = []        # MDL strings for buttons above the grid
        rowbtns = []      # MDL strings for per-row buttons
        needs_multi = False
        onclick = None
        skip_default = False
        sel_expr_row = {name: '$currentObject'}
        for b in items:
            bt = b['$Type']
            bname = b['name']
            if bt == 'Pages$GridSearchButton':
                self.buttons['search button -> dropped (column filters are always visible)'] += 1
                continue
            if bt == 'Pages$GridSelectAllButton' or bt == 'Pages$GridDeselectAllButton':
                self.buttons['select/deselect all -> dropped (DG2 header checkbox)'] += 1
                self.gap(unit, name, 'select all/deselect all button %s dropped (DG2 selection header instead)' % bname)
                continue
            if bt == 'Pages$DataGridExportToExcelButton':
                self.buttons['export to Excel -> dropped'] += 1
                self.gap(unit, name, 'export to Excel button %s dropped; DG2 exports via its own export dialog only when configured' % bname)
                continue
            if bt == 'Pages$SelectButton':
                self.buttons['select button -> dropped (selection page replaced by combo box)'] += 1
                continue
            if bt != 'Pages$GridActionButton':
                self.gap(unit, name, 'unknown control bar item %s' % bt); continue
            cap = txt(b['caption'])
            if b['caption'].get('parameters'):
                self.gap(unit, name, 'button %s: caption parameters dropped' % bname)
            a = b['action']
            mapped_self = False
            list_param = False
            ms = None
            if a['$Type'] == 'Pages$MicroflowClientAction':
                ms = a['microflowSettings']
            elif a['$Type'] == 'Pages$PageClientAction':
                ms = a['pageSettings']
            if ms:
                self.implicit_selection(a, ms, name, entity)
                mapped_self = any((m.get('variable') or {}).get('widget') == name for m in ms['parameterMappings'])
                if a['$Type'] == 'Pages$MicroflowClientAction':
                    params = self.M.mf_params.get(ms['microflow'], [])
                    for m in ms['parameterMappings']:
                        if (m.get('variable') or {}).get('widget') == name:
                            pn = m['parameter'].split('.')[-1]
                            list_param |= any(p[0] == pn and p[1] == 'list' for p in params)
            if a['$Type'] == 'Pages$DeleteClientAction': mapped_self = True
            style = b.get('buttonStyle') or 'Default'
            bprops = ['Caption: %s' % q(cap)]
            tip = txt(b.get('tooltip'))
            if tip: bprops.append('Tooltip: %s' % q(tip))
            if style != 'Default': bprops.append('ButtonStyle: %s' % style)
            if b.get('icon'): self.gap(unit, name, 'button %s: icon dropped' % bname)
            if mapped_self and list_param:
                act = self.action(a, gctx, unit, name, selmap={name: '$' + name})
                if act == '': continue
                needs_multi = True
                bprops.append('Action: %s' % act)
                above.append('ACTIONBUTTON %s (%s)' % (bname, ', '.join(bprops)))
                self.buttons['selection microflow (list) -> button above grid on $%s selection' % name] += 1
            elif mapped_self:
                act = self.action(a, gctx, unit, name, selmap=sel_expr_row)
                if act == '': continue
                bprops.append('Action: %s' % act)
                rowbtns.append((b['$ID'], 'ACTIONBUTTON %s (%s)' % (bname, ', '.join(bprops))))
                self.buttons['row action -> action column button on $currentObject'] += 1
            else:
                act = self.action(a, ctx, unit, name)
                if act == '': continue
                bprops.append('Action: %s' % (act if act else 'NOTHING'))
                above.append('ACTIONBUTTON %s (%s)' % (bname, ', '.join(bprops)))
                self.buttons['no selection needed -> button above grid'] += 1
            if default_id == b['$ID'] and bt == 'Pages$GridActionButton':
                onclick = act if mapped_self and not list_param else None
                if mapped_self and list_param:
                    skip_default = True
                    self.gap(unit, name, 'default (double click) action of button %s takes the selection list; kept as button above the grid, no row click action' % bname)
        if default_id and onclick is None and not skip_default:
            for b in items:
                if b['$ID'] == default_id:
                    if b['$Type'] == 'Pages$SelectButton':
                        pass
                    elif b['$Type'] == 'Pages$GridActionButton':
                        a = b['action']
                        act = self.action(a, gctx, unit, name, selmap=sel_expr_row)
                        if act: onclick = act
                    else:
                        self.gap(unit, name, 'default button %s of type %s not converted' % (b['name'], b['$Type']))
        # ---- assemble
        gp = ['DataSource: %s' % dsrc]
        sm = g.get('selectionMode')
        if needs_multi: gp.append('Selection: Multi')
        elif name in self.listen: gp.append('Selection: Single'); self.notes['grid listened to by a data view: Selection Single'] += 1
        elif sm in ('Multi', 'SimpleMulti') and False: gp.append('Selection: Multi')
        n = g.get('numberOfRows') or 20
        gp.append('PageSize: %s' % n)
        if g.get('showPagingBar') == 'No': gp.append("ShowPagingButtons: 'auto'")
        if onclick:
            gp.append('OnClick: %s' % onclick)
            gp.append("onClickTrigger: '%s'" % ('double' if g.get('defaultButtonTrigger') == 'Double' else 'single'))
        gp += self.common(g, unit, ctx)
        lines = ['DATAGRID %s (%s) {' % (name, ', '.join(gp))]
        for c in cols:
            props = list(c['props'])
            if c['filter']:
                lines.append('  COLUMN (%s) { %s }' % (', '.join(props), c['filter']))
            else:
                lines.append('  COLUMN (%s)' % ', '.join(props))
        if rowbtns:
            used_names.update(['%s_actions' % name])
            lines.append("  COLUMN (ShowContentAs: customContent, Caption: '', Sortable: false, Resizable: false, Draggable: false, Hidable: no, Alignment: right, ColumnWidth: autoFit) {")
            for _, rb in rowbtns:
                lines.append('    ' + rb)
            lines.append('  }')
        lines.append('}')
        grid = '\n'.join(lines)
        if above:
            wrap = '%s_wrap' % name
            i = 1
            while wrap in used_names:
                i += 1; wrap = '%s_wrap%d' % (name, i)
            used_names.add(wrap)
            grid = 'CONTAINER %s {\n%s\n%s\n}' % (wrap, '\n'.join(above), grid)
        self.notes['grid columns: %d' % 0] += 0
        return grid

    def implicit_selection(self, a, ms, gname, gentity):
        """Classic grid buttons get the grid selection for any unmapped parameter of the grid's entity."""
        if a['$Type'] == 'Pages$MicroflowClientAction':
            params = self.M.mf_params.get(ms['microflow'], [])
        elif a['$Type'] == 'Pages$PageClientAction':
            params = [(n, 'object', e) for (n, e) in self.M.page_params.get(ms['page'], [])]
        else:
            return
        have = {m['parameter'].split('.')[-1] for m in ms['parameterMappings']}
        for (pn, kind, ent) in params:
            if pn in have or kind not in ('list', 'object') or not gentity: continue
            if self.M.is_a(gentity, ent):
                ms['parameterMappings'] = ms['parameterMappings'] + [{
                    'parameter': 'x.x.' + pn, 'variable': {'widget': gname}, 'expression': ''}]
                self.notes['implicit grid selection parameter made explicit'] += 1

    def conv_templategrid(self, w, unit, ctx, used_names=None, kind='PAGE'):
        name = w['name']
        ds = w['dataSource']
        if ds.get('$Type') != 'Pages$GridXPathSource' or (ds.get('entityRef') or {}).get('$Type') != 'DomainModels$DirectEntityRef':
            self.gap(unit, name, 'template grid with data source %s not converted' % ds.get('$Type')); return None
        entity = ds['entityRef']['entity']
        xpc = xp(ds.get('xPathConstraint') or '')
        srt = self.sort_clause(ds.get('sortBar'), entity)
        gctx = ctx + [(entity, '$currentObject')]
        bad = []
        body = self.tg_content(w['contents'], unit, gctx, bad)
        if bad:
            self.gap(unit, name, 'template grid not converted, content has %s' % ', '.join(sorted(set(bad)))); return None
        if (w.get('controlBar') or {}).get('items'):
            self.gap(unit, name, 'template grid control bar buttons dropped')
        if (ds.get('searchBar') or {}).get('items'):
            self.gap(unit, name, 'template grid search fields dropped')
        gp = ['DataSource: DATABASE %s%s%s' % (entity, (' WHERE ' + xpc) if xpc else '', srt), 'PageSize: %s' % (w.get('numberOfRows') or 20)]
        nc = int(w.get('numberOfColumns') or 1)
        gp += ['DesktopColumns: %d' % nc, 'TabletColumns: %d' % min(nc, 2), 'PhoneColumns: 1']
        gp += self.common(w, unit, ctx)
        self.notes['template grid -> gallery'] += 1
        return 'GALLERY %s (%s) {\n%s\n}' % (name, ', '.join(gp), body)

    def tg_content(self, o, unit, ctx, bad):
        out = []
        if isinstance(o, dict):
            t = o.get('$Type')
            if t == 'Pages$TemplateGridContents':
                for x in o.get('widgets', []): out.append(self.tg_content(x, unit, ctx, bad))
                return '\n'.join(x for x in out if x)
            if t == 'Pages$DivContainer':
                kids = '\n'.join(x for x in (self.tg_content(c, unit, ctx, bad) for c in o.get('widgets', [])) if x)
                p = self.common(o, unit, ctx)
                if o.get('onClickAction') and o['onClickAction']['$Type'] != 'Pages$NoClientAction': bad.append('container click action')
                return 'CONTAINER %s%s {\n%s\n}' % (o['name'], (' (%s)' % ', '.join(p)) if p else '', kids)
            if t == 'Pages$DynamicText':
                c = o['content']
                if c.get('parameters'): bad.append('dynamic text with parameters')
                rm = {'Text': None, 'H1': 'H1', 'H2': 'H2', 'H3': 'H3', 'H4': 'H4', 'H5': 'H5', 'H6': 'H6', 'Paragraph': 'Paragraph'}.get(o.get('renderMode'))
                p = ['Content: %s' % q(txt(c))]
                if rm: p.append('RenderMode: %s' % rm)
                p += self.common(o, unit, ctx)
                return 'DYNAMICTEXT %s (%s)' % (o['name'], ', '.join(p))
            if t == 'Pages$StaticImageViewer':
                r = self.conv_image(o, unit, 'PAGE', ctx)
                if r is None: bad.append('image')
                return r
            if t == 'CustomWidgets$CustomWidget':
                self.gap(unit, o.get('name'), 'pluggable widget %s inside a converted template grid dropped (not auto-converted)' % ((o.get('type') or {}).get('widgetId') if isinstance(o.get('type'), dict) else ''))
                return ''
            bad.append(t.split('$')[-1] if t else 'unknown')
        return ''


# ------------------------------------------------------------------ traversal
MODEL = None
CUR_TARGETS = {}


def is_native(u):
    t = u['$Type']
    if t == 'Pages$Snippet': return u.get('type') == 'Native'
    if t == 'Pages$Page':
        lay = (u.get('layoutCall') or {}).get('layout') or ''
        return 'Native' in lay.split('.')[-1]
    if t == 'Pages$Layout': return 'Native' in u['$QualifiedName'].split('.')[-1]
    return False


def entity_of_source(ds):
    if not ds: return None
    ms = ds.get('microflowSettings') or ds.get('dataSourceMicroflowSettings')
    if ms and MODEL:
        mf = MODEL.byq.get(ms['microflow']) or {}
        return (mf.get('microflowReturnType') or {}).get('entity')
    if ds.get('$Type') == 'Pages$NanoflowSource' and MODEL:
        nf = MODEL.byq.get(ds.get('nanoflow')) or {}
        return (nf.get('microflowReturnType') or {}).get('entity')
    if ds.get('$Type') == 'Pages$ListenTargetSource':
        return CUR_TARGETS.get(ds['listenTarget'])
    er = ds.get('entityRef')
    if not er: return None
    if er['$Type'] == 'DomainModels$DirectEntityRef': return er['entity']
    return er['steps'][-1]['destinationEntity']


def walk(C, o, unit, kind, ctx, used, out):
    """collect legacy widgets in document order with their enclosing context"""
    if isinstance(o, list):
        for v in o: walk(C, v, unit, kind, ctx, used, out)
        return
    if not isinstance(o, dict): return
    t = o.get('$Type')
    if t in LEGACY:
        out.append((o, list(ctx)))
        return
    nctx = ctx
    if t == 'Pages$DataView':
        ds = o.get('dataSource') or {}
        sv = C.var(ds.get('sourceVariable'))
        ent = entity_of_source(ds)
        expr = sv or ('$' + o['name'])
        if ds.get('$Type') == 'Pages$ListenTargetSource': expr = '$currentObject'
        nctx = ctx + [(ent, expr)]
    elif t in ('Pages$ListView',):
        ds = o.get('dataSource') or {}
        nctx = ctx + [(entity_of_source(ds), '$currentObject')]
    for k, v in o.items():
        if isinstance(v, (dict, list)):
            walk(C, v, unit, kind, nctx, used, out)


def all_names(o, acc):
    if isinstance(o, dict):
        n = o.get('name')
        if isinstance(n, str): acc.add(n)
        for v in o.values(): all_names(v, acc)
    elif isinstance(o, list):
        for v in o: all_names(v, acc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dump'); ap.add_argument('out')
    ap.add_argument('--module'); ap.add_argument('--only'); ap.add_argument('--gaps')
    ap.add_argument('--notes')
    a = ap.parse_args()
    d = json.load(open(a.dump, encoding='utf-8-sig'))
    global MODEL
    M = Model(d)
    M.build_assoc()
    MODEL = M
    C = Conv(M)
    stmts = []
    units = sorted([u for u in M.units if u['$Type'] in UNIT_KINDS], key=lambda u: u['$QualifiedName'])
    for u in units:
        qn = u['$QualifiedName']
        if a.module and mod(qn) != a.module: continue
        if a.only and qn != a.only: continue
        if is_native(u):
            C.notes['native unit skipped (legacy widgets are valid on native pages): %s' % u['$Type'].split('$')[1]] += 1
            continue
        if u.get('excluded'):
            n_ex = sum(1 for _ in find(u, 'Pages$DataGrid')) + 0
            C.notes['excluded unit skipped: ' + qn] += 1
            continue
        kind = UNIT_KINDS[u['$Type']]
        ctx0 = []
        for (pn, ent) in M.page_params.get(qn, []):
            ctx0.append((ent, '$' + pn))
        found = []
        global CUR_TARGETS
        CUR_TARGETS = {}
        C.listen = collections.defaultdict(list)
        for t_ in ('Pages$DataGrid', 'Pages$ListView', 'Pages$TemplateGrid'):
            for x in find(u, t_):
                CUR_TARGETS[x['name']] = entity_of_source(x.get('dataSource'))
        for dv in find(u, 'Pages$DataView'):
            if dv['dataSource']['$Type'] == 'Pages$ListenTargetSource':
                C.listen[dv['dataSource']['listenTarget']].append(dv['name'])
        walk(C, u, qn, kind, ctx0, set(), found)
        if not found: continue
        used = set(); all_names(u, used)
        for w, ctx in found:
            sub = set(); all_names(w, sub); used -= sub
            t = LEGACY[w['$Type']]
            C.counts[t] += 1
            try:
                if t == 'DataGrid' or t == 'ReferenceSetSelector':
                    if t == 'ReferenceSetSelector':
                        ww = dict(w); ww['dataSource'] = w['dataSource']; ww['controlBar'] = w['controlBar']
                        ww['columns'] = w.get('columns', [])
                        mdl = C.conv_grid(ww, qn, ctx, used, kind)
                    else:
                        mdl = C.conv_grid(w, qn, ctx, used, kind)
                elif t in ('ReferenceSelector', 'InputReferenceSetSelector'):
                    mdl = C.conv_refselector(w, qn, ctx)
                elif t == 'DropDown':
                    mdl = C.conv_dropdown(w, qn, ctx)
                elif t in ('StaticImageViewer', 'DynamicImageViewer'):
                    mdl = C.conv_image(w, qn, kind, ctx)
                elif t == 'TemplateGrid':
                    mdl = C.conv_templategrid(w, qn, ctx, used, kind)
            except Exception as e:  # keep going, log
                C.gap(qn, w.get('name'), 'generator error: %r' % e)
                mdl = None
            if mdl is None:
                C.counts['skipped:' + t] += 1
                continue
            C.counts['emitted:' + t] += 1
            extra = ''.join('ALTER %s %s {\n  SET (DataSource: SELECTION %s) ON %s;\n};\n' % (kind, qn, w['name'], dvn)
                            for dvn in C.listen.get(w['name'], [])) if t == 'DataGrid' else ''
            stmts.append(extra and '' or '')
            stmts.append('-- %s %s (%s)\nALTER %s %s {\n  REPLACE %s WITH {\n%s\n  };\n};\n' % (
                kind, qn, t, kind, qn, w['name'], '\n'.join('    ' + l for l in mdl.split('\n'))) + extra)
    with open(a.out, 'w') as f:
        f.write('mdl 1;\n-- generated by convert_legacy.py (deterministic)\n\n')
        f.write('\n'.join(stmts))
    for k in sorted(C.counts): print('%-40s %d' % (k, C.counts[k]))
    print('gaps:', len(C.gaps))
    if a.gaps: json.dump(C.gaps, open(a.gaps, 'w'), indent=1)
    if a.notes:
        json.dump({'notes': C.notes, 'buttons': C.buttons}, open(a.notes, 'w'), indent=1)


if __name__ == '__main__':
    main()
