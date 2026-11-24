---
title: Migrating a custom pluggable widget from Webpack (tools 8.x) to Rollup
topic: upgrade
domain: [ux-ui, delivery-process]
kind: procedure
applies_to: company-standard
versions: "pluggable-widgets-tools 8.x -> ^10.18 (>= 10.18.2 for custom rollup config); works on Mx9+"
keywords: ["Webpack to Rollup migration", "pluggable widgets tools upgrade", "webpack.config.js removal", "rollup.config.js", "Node 20", "piw-utils-internal dependency", "widget icons svg", "package.json tools version", "custom rollup config", "mpk build", "Mx9 Mx10 support"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- A widget built with tools 8.x (Webpack) needs to work on newer Mendix.
- One widget team also bumped React dev dependencies from 17 to 18 for 9.24.

**Steps**
1. Set `@mendix/pluggable-widgets-tools` to `^10.18.0` in `package.json`. This also works on Mx9.
2. Set Node 20 in `package.json` and `.nvmrc`.
3. Port any custom logic from `webpack.config.dev.js` and `webpack.config.prod.js`.
4. Put toolbox icons in the root `src` folder so no rollup config is needed:
   - `{widget}.icon.png` (64x64) and `{widget}.icon.dark.png`;
   - `{widget}.tile.png` (256x192) and `{widget}.tile.dark.png`.
5. Remove the local `piw-utils-internal` dependency.
   - Import typings from pluggable-widgets-tools.
   - Copy `structure-preview-api.ts` from the pds-template-widget repo.
6. Remove the Webpack dependencies.
7. Run `nvm use 20` and then `npm install`.
8. To import SVGs, add `svg.d.ts` declaring `*.svg` as a string. Only wrap an SVG in a component if you need props.
9. If you still need a custom config, export `args => …` in `rollup.config.js` and extend `args.configDefaultConfig`.

**Checks**
- The build produces an mpk with icons.

**Watch out**
- Some tools versions fail to build with a custom rollup config. Use at least 10.18.2.
