#!/usr/bin/env python3
"""mkjarstale.py: jar folders for the jardedupe STALE / OLD-VERSION controls (public library names, real zips).

  mkjarstale.py <out dir> addon-cache|addon-zip|addon-unreadable|no-addon|sso|t1r|n3|netty|netty-nocodec|artifact|artifact-pkg|artifact-unknown|artifact-extras|artifact-shaded|artifact-addon|artifact-leftover

addon-*   T2R3-6 shape: the 6 OIDC-marked userlib jars of TOOLKIT-FEEDBACK T2R3-6 (java-jwt 3.11.0, jackson-core,
          -databind, -annotations 2.14.1, json, commons-codec 1.15), no OIDC module in the app, and an add-on
          MFN_Authentication whose DecodeJWT.java imports com.auth0.jwt and jackson databind. A PushNotifications-marked
          jar nobody imports stays stale. -cache: the Java is in .mendix-cache/modules/mfn_authentication.mxmodule/
          (where the worker found it); -zip: only inside modules/MFN_Authentication.mxmodule; -unreadable: the
          .mxmodule is no zip and there is no cache; no-addon: the same jars without any add-on.
sso       N3-17 marker shape '<jar>.MendixSSO.<version>.RequiredLib': old-only jars, a jar both versions claim, an orphan
          marker, an old-only jar the app's javasource imports.
t1r       T1R-13: the userlib pairs of runs/t1r2-purchase-request evidence/jarclash-before.md, unversioned MendixSSO markers.
n3        N3-17: the vendorlib pairs of runs/n3-purchase-request-11 evidence/jarclash-11.md, plus orphan MendixSSO.4.1.0
          markers.
netty     NS-3: notification-service a06afe60, cut down: MendixSSO-marked netty 4.1.119.Final jars in userlib, netty
          4.2.5.Final in vendorlib, where 4.2 split netty-codec into netty-codec-base and netty-codec-compression.
          userlib/netty-codec-4.1.119.Final.jar has no copy anywhere; -nocodec: the same without it.
artifact  GM-27: kotlin-stdlib and annotations jars whose marker names the ARTIFACT 'databroker-business-events-module',
          not the module (BusinessEvents, which IS in the app: javasource/businessevents/ imports the artifact jar's
          package). Also a jar marked by OldMod, a module the app no longer has: that one is still STALE.
artifact-pkg   the same markers, but nothing in the Java links them: only the module's installed package (an .mpk in
          the cache the control writes) ships the marker files.
artifact-extras   the owner's Java imports a package of '<artifact>-extras-1.jar', which is another artifact: no claim.
artifact-shaded   the artifact jar holds only com.google.gson, which gson-2.10.jar provides too, and an unrelated module
          'other' imports com.google.gson.Gson: a shared package proves nothing.
artifact-addon    the artifact jar's package is imported by an add-on's Java only (.mendix-cache/modules/...).
artifact-leftover a javasource/oldmod/ folder imports the artifact jar's package, but OldMod is not installed.
artifact-unknown   the artifact marker with no owner anywhere (no package, no jar, no Java), plus the OldMod jar.
"""
import io, os, sys, zipfile


def jar(classes, maven=None):
    b = io.BytesIO()
    with zipfile.ZipFile(b, "w") as z:
        z.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n")
        for c in classes:
            z.writestr(c, b"\xca\xfe\xba\xbe")
        if maven:
            g, a, v = maven
            z.writestr(f"META-INF/maven/{g}/{a}/pom.properties", f"groupId={g}\nartifactId={a}\nversion={v}\n")
    return b.getvalue()


def put(path, data=b""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "wb").write(data if isinstance(data, bytes) else data.encode())


def cls(pkg, n=3):
    return [f"{pkg.replace('.', '/')}/C{i}.class" for i in range(n)]


out, kind = sys.argv[1], sys.argv[2]
os.makedirs(f"{out}/userlib", exist_ok=True)
os.makedirs(f"{out}/vendorlib", exist_ok=True)
if kind.startswith("addon") or kind == "no-addon":
    put(f"{out}/App.mpr", "Module StarterKit Module Administration")
    for name, pkg, mvn in (("java-jwt-3.11.0.jar", "com.auth0.jwt", ("com.auth0", "java-jwt", "3.11.0")),
                           ("jackson-core-2.14.1.jar", "com.fasterxml.jackson.core", ("com.fasterxml.jackson.core", "jackson-core", "2.14.1")),
                           ("jackson-databind-2.14.1.jar", "com.fasterxml.jackson.databind", ("com.fasterxml.jackson.core", "jackson-databind", "2.14.1")),
                           ("jackson-annotations-2.14.1.jar", "com.fasterxml.jackson.annotation", ("com.fasterxml.jackson.core", "jackson-annotations", "2.14.1")),
                           ("json-20220924.jar", "org.json", ("org.json", "json", "20220924")),
                           ("commons-codec-1.15.jar", "org.apache.commons.codec", ("commons-codec", "commons-codec", "1.15"))):
        put(f"{out}/userlib/{name}", jar(cls(pkg), mvn))
        put(f"{out}/userlib/{name}.OIDC.RequiredLib")
    put(f"{out}/userlib/pushy-0.15.2.jar", jar(cls("com.eatthepath.pushy.apns"), ("com.eatthepath", "pushy", "0.15.2")))
    put(f"{out}/userlib/pushy-0.15.2.jar.PushNotifications.RequiredLib")
    java = ("package mfn_authentication.actions;\n\nimport com.auth0.jwt.JWT;\nimport com.auth0.jwt.interfaces.DecodedJWT;\n"
            "import com.fasterxml.jackson.databind.ObjectMapper;\nimport com.mendix.systemwideinterfaces.core.IContext;\n\n"
            "public class DecodeJWT {}\n")
    rel = "javasource/mfn_authentication/actions/DecodeJWT.java"
    if kind == "addon-cache":
        put(f"{out}/modules/MFN_Authentication.mxmodule", jar(["project.mpr"]))
        put(f"{out}/.mendix-cache/modules/mfn_authentication.mxmodule/{rel}", java)
    elif kind == "addon-zip":
        b = io.BytesIO()
        with zipfile.ZipFile(b, "w") as z:
            z.writestr("project.mpr", b"")
            z.writestr(rel, java)
        put(f"{out}/modules/MFN_Authentication.mxmodule", b.getvalue())
    elif kind == "addon-unreadable":
        put(f"{out}/modules/MFN_Authentication.mxmodule", "notazip")
elif kind == "sso":
    put(f"{out}/App.mpr", "Module MendixSSO Module Administration")
    put(f"{out}/userlib/accessors-smart-2.4.7.jar", jar(cls("net.minidev.asm"), ("net.minidev", "accessors-smart", "2.4.7")))
    put(f"{out}/userlib/accessors-smart-2.4.7.jar.MendixSSO.4.1.0.RequiredLib")
    put(f"{out}/userlib/accessors-smart-2.4.9.jar", jar(cls("net.minidev.asm"), ("net.minidev", "accessors-smart", "2.4.9")))
    put(f"{out}/userlib/accessors-smart-2.4.9.jar.MendixSSO.4.2.0.RequiredLib")
    put(f"{out}/userlib/jcip-annotations-1.0-1.jar", jar(cls("net.jcip.annotations"), ("com.github.stephenc.jcip", "jcip-annotations", "1.0-1")))
    put(f"{out}/userlib/jcip-annotations-1.0-1.jar.MendixSSO.4.1.0.RequiredLib")
    put(f"{out}/userlib/commons-lang3-3.12.0.jar", jar(cls("org.apache.commons.lang3"), ("org.apache.commons", "commons-lang3", "3.12.0")))
    put(f"{out}/userlib/commons-lang3-3.12.0.jar.MendixSSO.4.1.0.RequiredLib")
    put(f"{out}/userlib/commons-lang3-3.12.0.jar.MendixSSO.4.2.0.RequiredLib")
    put(f"{out}/userlib/lang-tag-1.5.jar", jar(cls("com.nimbusds.langtag"), ("com.nimbusds", "lang-tag", "1.5")))
    put(f"{out}/userlib/lang-tag-1.5.jar.MendixSSO.4.1.0.RequiredLib")
    put(f"{out}/userlib/oauth2-oidc-sdk-9.15.jar.MendixSSO.4.1.0.RequiredLib")   # orphan: the jar is gone
    put(f"{out}/javasource/mendixsso/actions/Tag.java", "import com.nimbusds.langtag.LangTag;\nclass Tag {}\n")
elif kind == "t1r":
    put(f"{out}/App.mpr", "Module MendixSSO")
    for a, g, vs, pkg in (("oauth2-oidc-sdk", "com.nimbusds", ("9.15", "10.7"), "com.nimbusds.oauth2.sdk"),
                          ("commons-lang3", "org.apache.commons", ("3.11", "3.12.0"), "org.apache.commons.lang3"),
                          ("nimbus-jose-jwt", "com.nimbusds", ("9.12.1", "9.29"), "com.nimbusds.jose"),
                          ("json-smart", "net.minidev", ("2.4.7", "2.4.10"), "net.minidev.json"),
                          ("asm", None, ("9.1", "9.3"), "org.objectweb.asm"),
                          ("accessors-smart", "net.minidev", ("2.4.7", "2.4.9"), "net.minidev.asm")):
        for v in vs:
            put(f"{out}/userlib/{a}-{v}.jar", jar(cls(pkg), (g, a, v) if g else None))
            put(f"{out}/userlib/{a}-{v}.jar.MendixSSO.RequiredLib")
elif kind == "n3":
    put(f"{out}/App.mpr", "Module MendixSSO")
    for a, g, vs, pkg in (("nimbus-jose-jwt", "com.nimbusds", ("9.30.2", "10.4.2"), "com.nimbusds.jose"),
                          ("oauth2-oidc-sdk", "com.nimbusds", ("10.7.1", "11.28"), "com.nimbusds.oauth2.sdk"),
                          ("commons-lang3", "org.apache.commons", ("3.12.0", "3.18.0"), "org.apache.commons.lang3"),
                          ("commons-text", "org.apache.commons", ("1.10.0", "1.14.0"), "org.apache.commons.text"),
                          ("json-smart", "net.minidev", ("2.4.10", "2.5.2"), "net.minidev.json"),
                          ("asm", None, ("9.3", "9.7.1"), "org.objectweb.asm"),
                          ("accessors-smart", "net.minidev", ("2.4.9", "2.5.2"), "net.minidev.asm")):
        for v in vs:
            put(f"{out}/vendorlib/{a}-{v}.jar", jar(cls(pkg), (g, a, v) if g else None))
    for a in ("nimbus-jose-jwt-9.12.1", "oauth2-oidc-sdk-9.15", "commons-lang3-3.11"):
        put(f"{out}/userlib/{a}.jar.MendixSSO.4.1.0.RequiredLib")
elif kind in ("netty", "netty-nocodec"):
    put(f"{out}/App.mpr", "Module MendixSSO")
    put(f"{out}/javasource/mendixsso/actions/Login.java", "package mendixsso.actions;\nclass Login {}\n")
    v1, v2 = "4.1.119.Final", "4.2.5.Final"
    for a in ("netty-buffer", "netty-codec-http") + (("netty-codec",) if kind == "netty" else ()):
        put(f"{out}/userlib/{a}-{v1}.jar", jar(cls("io.netty." + a.split("-", 1)[1].replace("-", ".")), ("io.netty", a, v1)))
        put(f"{out}/userlib/{a}-{v1}.jar.MendixSSO.RequiredLib")
    for a in ("netty-buffer", "netty-codec-http", "netty-codec-base", "netty-codec-compression"):
        put(f"{out}/vendorlib/{a}-{v2}.jar", jar(cls("io.netty." + a.split("-", 1)[1].replace("-", ".")), ("io.netty", a, v2)))
elif kind in ("artifact", "artifact-pkg", "artifact-unknown", "artifact-extras", "artifact-shaded", "artifact-addon",
              "artifact-leftover"):
    art = "databroker-business-events-module"
    put(f"{out}/App.mpr", "Module BusinessEvents Module Administration")
    for a, g, v, pkg in (("kotlin-stdlib", "org.jetbrains.kotlin", "1.9.10", "kotlin"),
                         ("annotations", "org.jetbrains", "13.0", "org.intellij.lang.annotations")):
        put(f"{out}/userlib/{a}-{v}.jar", jar(cls(pkg), (g, a, v)))
        put(f"{out}/userlib/{a}-{v}.jar.{art}.RequiredLib")
    put(f"{out}/userlib/pushy-0.15.2.jar", jar(cls("com.eatthepath.pushy.apns"), ("com.eatthepath", "pushy", "0.15.2")))
    put(f"{out}/userlib/pushy-0.15.2.jar.OldMod.RequiredLib")   # OldMod is not in the app: truly stale
    if kind == "artifact":
        put(f"{out}/userlib/{art}-3.12.1.jar", jar(cls("com.mendix.businessevents.runtime"), ("com.mendix", art, "3.12.1")))
        put(f"{out}/javasource/businessevents/actions/Publish.java",
            "package businessevents.actions;\nimport com.mendix.businessevents.runtime.C0;\nclass Publish {}\n")
    elif kind == "artifact-extras":
        put(f"{out}/userlib/{art}-extras-1.jar", jar(cls("com.mendix.businessevents.extras")))
        put(f"{out}/javasource/businessevents/actions/Publish.java",
            "package businessevents.actions;\nimport com.mendix.businessevents.extras.C0;\nclass Publish {}\n")
    elif kind == "artifact-shaded":
        put(f"{out}/App.mpr", "Module BusinessEvents Module other Module Administration")
        put(f"{out}/userlib/{art}-3.12.1.jar", jar(cls("com.google.gson")))
        put(f"{out}/userlib/gson-2.10.jar", jar(cls("com.google.gson"), ("com.google.code.gson", "gson", "2.10")))
        put(f"{out}/javasource/other/actions/Parse.java",
            "package other.actions;\nimport com.google.gson.Gson;\nclass Parse {}\n")
    elif kind == "artifact-addon":
        put(f"{out}/userlib/{art}-3.12.1.jar", jar(cls("com.mendix.businessevents.runtime")))
        put(f"{out}/.mendix-cache/modules/businessevents.mxmodule/javasource/businessevents/actions/Publish.java",
            "package businessevents.actions;\nimport com.mendix.businessevents.runtime.C0;\nclass Publish {}\n")
    elif kind == "artifact-leftover":
        put(f"{out}/userlib/{art}-3.12.1.jar", jar(cls("com.mendix.businessevents.runtime")))
        put(f"{out}/javasource/oldmod/actions/Publish.java",
            "package oldmod.actions;\nimport com.mendix.businessevents.runtime.C0;\nclass Publish {}\n")
    elif kind == "artifact-pkg":
        put(f"{out}/javasource/businessevents/actions/Publish.java", "package businessevents.actions;\nclass Publish {}\n")
        z = io.BytesIO()
        with zipfile.ZipFile(z, "w") as zf:
            for a, v in (("kotlin-stdlib", "1.9.10"), ("annotations", "13.0")):
                zf.writestr(f"userlib/{a}-{v}.jar.{art}.RequiredLib", "")
        put(f"{out}/pkgcache/170-3.12.1.mpk", z.getvalue())
else:
    sys.exit(f"mkjarstale: unknown kind {kind}")
