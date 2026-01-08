# Roadmap: Frankfurt la Torre 2 - Web

Data: 2026-01-08
Versio: 1.0

## Resum

Landing page Astro amb 5 seccions + integració SmartMenu Agora.

---

## Fase 1: Setup Projecte

**Objectiu:** Projecte Astro funcional amb estructura base.

### Tasques
- [ ] Inicialitzar projecte Astro
- [ ] Configurar estructura de carpetes
- [ ] Afegir Google Fonts (Archivo Black, DM Sans)
- [ ] Crear variables CSS (colors, tipografia)
- [ ] Verificar que compila correctament

### Resultat
```
npm run dev -> localhost:4321 funcionant
```

---

## Fase 2: Layout i Estils Base

**Objectiu:** Layout responsive amb estils globals.

### Tasques
- [ ] Crear Layout.astro amb meta tags SEO
- [ ] Definir estils globals (reset, variables, tipografia)
- [ ] Crear sistema de grid/contenidor responsive
- [ ] Afegir favicon i manifest bàsic

### Components
- `Layout.astro` - Layout principal
- `styles/global.css` - Estils globals

---

## Fase 3: Components Principals

**Objectiu:** Tots els components de la landing.

### 3.1 Header + Hero
- [ ] Header amb logo i CTA
- [ ] Hero amb títol, subtítol i botó principal
- [ ] Imatge de fons o gradient

### 3.2 Productes Estrella
- [ ] Component ProductCard
- [ ] Grid de 6 productes (placeholders)
- [ ] Hover effects

### 3.3 Nosaltres
- [ ] Secció amb text sobre el restaurant
- [ ] Imatge o icones decoratives

### 3.4 Contacte + Mapa
- [ ] Adreça, telèfon, horaris
- [ ] Embed Google Maps (placeholder)
- [ ] Botons d'acció (trucar, WhatsApp)

### 3.5 Footer
- [ ] Links xarxes socials
- [ ] Copyright
- [ ] Link legal (futur)

### 3.6 CTA Flotant
- [ ] Botó fix a la cantonada
- [ ] Link a SmartMenu

### Components
- `Header.astro`
- `Hero.astro`
- `ProductCard.astro`
- `ProductsSection.astro`
- `About.astro`
- `Contact.astro`
- `Footer.astro`
- `FloatingCTA.astro`

---

## Fase 4: SEO i Optimització

**Objectiu:** Optimitzar per cercadors i rendiment.

### Tasques
- [ ] Meta tags complets (title, description, OG)
- [ ] Schema.org per restaurant local
- [ ] Optimitzar imatges (format webp)
- [ ] Verificar Lighthouse score > 90

---

## Fase 5: Testing i Deploy

**Objectiu:** Publicar la landing.

### Tasques
- [ ] Test en mòbil i desktop
- [ ] Verificar tots els links
- [ ] Deploy a Vercel/Netlify
- [ ] Configurar domini (si disponible)

---

## Dependències Externes

| Element | Estat | Nota |
|---------|-------|------|
| URL SmartMenu | Pendent | Necessita ID client Agora |
| Fotos productes | Pendent | Usarem placeholders |
| Coordenades mapa | Pendent | Adreça aproximada |

---

## Ordre d'Implementació

```
Fase 1 (Setup) -> Fase 2 (Layout) -> Fase 3 (Components) -> Fase 4 (SEO) -> Fase 5 (Deploy)
```

Cada fase requereix confirmació abans de continuar.
