---
title: Replacing the Deeplink module with page/microflow URLs while keeping OIDC SSO
topic: upgrade
domain: [security, integration]
kind: procedure
applies_to: mendix-general
versions: "Mx10 (source example uses 10.5)"
keywords: ["Deeplink module replacement", "page URLs OIDC", "SSO deep linking", "originURI script", "oauth/v2/login", "cont parameter", "IdP button nanoflow", "login forward service", "anchor to query parameter", "session restoration hash", "infinite redirect loop", "access denied login hint"]
layer: field
sources:
  - {title: "Mendix field experience (internal sources not published)"}
confidentiality: public
status: draft-unreviewed
---
**When**
- You drop Deeplink and use SSO.
- With page URLs, Deeplink's `LoginLocation` has no equivalent. A user without access just gets the standard login page.
- With local accounts only, page URLs work out of the box.

**Steps**
1. Copy `index.html` from `<Studio Pro>\modeler\runtemplates\deployment\dojo-web\` into `theme/web`.
2. Replace the originURI script at the bottom. Remove the `if` so users don't get stuck on `login.html`. Use:
   `document.cookie = \`originURI=${subPath}/login/forward${https ? ";SameSite=None;Secure" : ""}\``
   where `subPath` is the path up to the last `/`.
3. Publish a service at `/login/forward` that returns HTML with JS.
   - The JS turns the `#/…` anchor into `?cont=/p/…` and redirects to `/p/login`.
   - It skips the parameter when the target is `/login`, to avoid loops.
   - The anchor never reaches the server, so this must be done client-side.
4. Make `/p/login` an anonymous home page with the login form and/or the IdP list.
5. The IdP button runs a nanoflow:
   - read `window.location.href`;
   - parse it (NativeMobileResources);
   - open `'/oauth/v2/login?idp=' + Alias + '&cont=' + cont`.

**Watch out**
- Local login needs the hash restored on the login page with `setTimeout(() => location.hash = …, 200)`.
- To strip the leftover `?cont`, call `history.replaceState` from the layout, not the home page.
- A logged-in user without access loops back to login. Show a hint when `cont` is present.
- Single IdP with auto sign-in: forward straight to `/oauth/v2/login`. This carries a high risk of an infinite redirect loop on pages the user cannot access.
- PWA support is unknown. Native is not supported. SAML should work the same way (unverified).
- Status: workaround from a field how-to (unreviewed). Its example implementation uses Mendix 10.5. The source says nothing about other versions.
