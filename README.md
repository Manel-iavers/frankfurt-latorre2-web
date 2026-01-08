# Frankfurt La Torre 2 - Web

Landing page per Frankfurt La Torre 2 (Pineda de Mar).

**Web:** https://latorre2.com

---

## Guia Ràpida de Gestió

### Mode Vacances

Edita el fitxer `src/config/site.ts`:

```typescript
vacation: {
  enabled: true,              // true = mostrar banner, false = ocultar
  returnDate: "13 de Febrer", // Data de tornada
  message: "Estem de vacances! Ens veiem aviat."
}
```

**Per activar vacances:** `enabled: true`
**Per desactivar vacances:** `enabled: false`

Després de canviar, fes commit i push per actualitzar la web.

---

### Sistema de Comandes (SmartMenu)

Edita el fitxer `src/config/site.ts`:

```typescript
smartMenuUrl: "#",  // Canvia "#" per l'URL de SmartMenu
```

**Exemple:**
```typescript
smartMenuUrl: "https://smartmenu.agora.com/latorre2",
```

Mentre l'URL sigui `"#"`, els botons "Fer Comanda" mostraran un modal dient que truquin per telèfon.

---

## Desplegament

La web es desplega automàticament a Vercel quan fas push a GitHub.

```bash
# Fer canvis i desplegar
git add .
git commit -m "descripció dels canvis"
git push
```

La web s'actualitza en ~1 minut.

---

## Desenvolupament Local

```bash
# Instal·lar dependències
npm install

# Servidor de desenvolupament
npm run dev

# Build de producció
npm run build
```

---

## Estructura de Fitxers

```
src/
├── config/
│   └── site.ts          # ⭐ Configuració (vacances, SmartMenu)
├── components/
│   ├── Header.astro
│   ├── Hero.astro
│   ├── ProductsSection.astro
│   ├── About.astro
│   ├── FAQ.astro
│   ├── Contact.astro
│   ├── Footer.astro
│   ├── FloatingCTA.astro
│   ├── VacationBanner.astro
│   └── ComingSoonModal.astro
├── pages/
│   ├── index.astro      # Pàgina principal
│   └── carta.astro      # Pàgina carta completa
└── layouts/
    └── Layout.astro     # SEO i Schema.org
```

---

## Contacte

- **Tel:** 687 985 175
- **Email:** latorre2frankfurt@gmail.com
- **Adreça:** Plaça Estació, 1 - 08397 Pineda de Mar
