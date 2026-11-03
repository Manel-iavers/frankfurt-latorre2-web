## Validate — frankfurt-latorre2-web — 2026-11-03
**Categoria**: Públic (web a domini públic)
**Fase**: migració a Cloudflare Workers (branca `chore/migracio-cloudflare`, PR #1)
**Resultat global**: ❌ FALLA (3 gates, tots heretats de `main`; cap introduït per la migració)

### Gates transversals
- ✅ Cap secret al codi
- ✅ `.env` al `.gitignore`
- ✅ Semgrep 1.168.0 (`p/default`, `p/javascript`, `p/secrets`; `--config=auto` no funciona amb `--metrics=off`): 0 troballes en 41 fitxers
- ❌ npm audit: **1 crític, 16 alts**. El crític és `astro` ≤7.3.1 (XSS a `define:vars`, bypass d'allowlist remota). La correcció és `astro@7.4.1`, un salt de versió major (avui 5.16.7). La resta són dependències de build (vite, rollup, postcss, sharp, zod…).
  - Exposició real: el web és HTML estàtic i cap d'aquests paquets no corre a producció. L'únic `define:vars` (`GoogleAnalytics.astro`) rep constants de `site.ts`, no cap entrada d'usuari.
- ✅ No placeholders
- ✅ Escriptura comptada: `scripts/check-routes.sh` no escriu res; compta errors i surt amb codi ≠ 0 si n'hi ha.
- ⚠️ Git net: `.claude/memory/session.md` modificat i `AGENTS.md` sense seguiment. No són d'aquesta feina.

### Gates d'stack (Astro estàtic)
- ✅ Build: net (`npm run build`, 2 pàgines)
- ➖ TypeScript / lint / tests: el projecte no en té configurats
- ✅ Rutes: `scripts/check-routes.sh` → 26×200 + 404 i cap `Set-Cookie`, contra workers.dev i contra producció
- ✅ HTML de `/` i `/carta` a workers.dev idèntic byte a byte a producció
- ❌ Lighthouse Performance (mòbil, llindar públic ≥85):
  - workers.dev: 70 / 81 / 80 (tres execucions)
  - Vercel: 81 / 87 (dues execucions)
  - Causa comuna: la pàgina pesa **7,5 MB** en PNG sense optimitzar (`burguerWeb.png` sol fa 1,37 MB). LCP de 4–5 s.
  - La diferència entre proveïdors és dins del soroll de Lighthouse.
- ✅ Lighthouse Accessibility: 96 (llindar ≥90) · Best Practices 100 · SEO 100

### Escenaris funcionals (Plan)
- ⚠️ No n'hi ha cap a `specs/`. El validate no és independent.

### No-regressió
- Creat `specs/regression-checklist.md` amb 4 features inferides.
- Pàgines servides ✅, carta ✅ (HTML idèntic a producció).
- CTA SmartMenu: el HTML és idèntic, però el clic no s'ha provat.
- GA4 condicionat al consentiment: pendent de verificar a mà.

### E2E smoke
- ❌ No hi ha cap test E2E. És obligatori per a un web amb UI.

### Accions necessàries
1. ❌ **Dependències:** pujar Astro 5 → 7 (salt major), en un PR a part i amb comparació visual. Alternativa: acceptar el risc documentat, perquè el web és estàtic.
2. ❌ **Performance:** convertir les imatges a WebP responsive (skill `image-optimization-pipeline`). És fora d'abast de la migració, que exclou canvis de contingut.
3. ❌ **E2E:** afegir un smoke test Playwright (home → CTA → carta).
4. ⚠️ Definir escenaris funcionals a `specs/`.
5. ⚠️ Corregir `site:` a `astro.config.mjs` (`frankfurtlatorre2.com` no resol; sitemap i canonical malament).

**Conclusió:** la migració no introdueix cap regressió (mateix HTML, mateixes rutes, cap cookie). Els tres ❌ ja eren a `main` i a producció abans d'aquest PR. No s'escriu `.last-validate`.
