# Regression Checklist — frankfurt-latorre2-web

_Creat: 2026-11-03_
_Última actualització: 2026-11-03_
_Manteniment: s'actualitza a cada `/retro` i es consulta a cada `/validate`_

---

## Com usar aquest fitxer

Aquest checklist llista les **features crítiques que mai s'han de trencar**. S'usa durant `/validate` com a smoke test de no-regressió.

### Regles

1. **Afegir entrada** quan una feature passa a producció (moment `/retro`).
2. **Actualitzar "Última verificació"** cada vegada que `/validate` la comprova amb èxit.
3. **Marcar com obsolet** (amb ~~strikethrough~~) si la feature es desactiva deliberadament — no esborrar.
4. **Prioritat**:
   - **Crítica**: si es trenca, el sistema no es pot usar (login, pagaments, auth).
   - **Alta**: si es trenca, un flux important queda bloquejat (generar doc, escanejar DNI).
   - **Mitjana**: si es trenca, afecta UX però hi ha workaround.

---

## Features crítiques

### Plantilla d'entrada

```markdown
### [Nom feature]
- **Happy path**: [descripció del que ha de funcionar]
- **Test automatitzat**: [ruta del test o "manual"]
- **Com verificar manualment**: [passos concrets]
- **Última verificació**: [YYYY-MM-DD]
- **Prioritat**: Crítica / Alta / Mitjana
- **Fase origen**: [Fase X — YYYY-MM-DD]
```

---

## Features del web (inferides del codi i de l'historial git, 03/11/2026)

### Pàgines servides
- **Happy path**: totes les rutes del build (`/`, `/carta`, imatges, CSS, `robots.txt`, `llms.txt`, sitemap) responen 200 i sense `Set-Cookie`
- **Test automatitzat**: `npm run build && scripts/check-routes.sh <URL>`
- **Com verificar manualment**: obrir `/` i `/carta` al mòbil
- **Última verificació**: 2026-11-03 (workers.dev i www.latorre2.com)
- **Prioritat**: Crítica
- **Fase origen**: MVP — 2026-01

### CTA «Fer comanda» cap al SmartMenu d'Àgora
- **Happy path**: el botó del hero i el botó flotant obren `smartMenuUrl` de `src/config/site.ts`
- **Test automatitzat**: manual
- **Com verificar manualment**: clicar «Fer comanda» → s'obre smartmenu.agorapos.com amb la carta del Frankfurt
- **Última verificació**: 2026-11-03 (HTML idèntic a producció; clic no provat)
- **Prioritat**: Crítica
- **Fase origen**: feat 2075ebc

### Carta amb preus
- **Happy path**: `/carta` mostra els entrepans amb preu interior i terrassa
- **Test automatitzat**: manual
- **Com verificar manualment**: comparar `/carta` amb la carta vigent del local
- **Última verificació**: 2026-11-03 (HTML idèntic a producció)
- **Prioritat**: Alta
- **Fase origen**: feat fa76696

### GA4 només amb consentiment
- **Happy path**: sense acceptar el banner no es carrega `googletagmanager.com`; en acceptar, sí
- **Test automatitzat**: manual
- **Com verificar manualment**: finestra privada → pestanya Network → cap petició a googletagmanager fins a clicar «Acceptar»
- **Última verificació**: pendent
- **Prioritat**: Alta
- **Fase origen**: CookieConsent + GoogleAnalytics

---

## Obsolets (no esborrar)

Llista de features que s'han desactivat. Serveix d'historial.

~~### [Feature antiga]~~
~~Raó desactivació: [motiu]~~
~~Data: [YYYY-MM-DD]~~
