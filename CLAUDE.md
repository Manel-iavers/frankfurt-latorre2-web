# Frankfurt la Torre 2 - Web

Landing page moderna per Frankfurt la Torre 2 (Pineda de Mar) amb integració SmartMenu Agora.

## Projecte

| Camp | Valor |
|------|-------|
| Nom | frankfurt-latorre2-web |
| Client | Frankfurt la Torre 2 |
| Stack | Astro |
| Deploy | Vercel/Netlify |

## AQUEST PROJECTE

### Visió
Landing page atractiva que converteixi visitants en clients, amb accés directe a comandes via SmartMenu Agora.

### Usuaris
Clients del restaurant que volen fer comandes per recollir.

### Funcionalitats MVP
1. Hero amb CTA "Fer Comanda" prominent
2. Secció productes estrella (6 destacats)
3. Secció "Nosaltres" + Ubicació/mapa/contacte
4. Botó flotant CTA sempre visible
5. Integració SmartMenu Agora

### Requisits Clau
- Mobile-first, responsive
- Ràpid (< 2s load time)
- SEO optimitzat
- Zero backend propi

### Decisions Pendents
- [ ] URL SmartMenu (pendent ID client)
- [ ] Fotos definitives productes

---

## Stack

- **Astro** - Framework principal (genera HTML estàtic)
- **CSS** - Estils (o Tailwind si es prefereix)
- **Google Fonts** - Archivo Black + DM Sans

## Disseny

### Colors
```css
--color-primary: #E8A936;    /* Groc mostassa */
--color-accent: #C41E3A;     /* Vermell */
--color-dark: #1A1A1A;       /* Negre */
--color-light: #FFF8E7;      /* Crema */
```

### Fonts
- **Títols:** Archivo Black
- **Cos:** DM Sans

## Estructura

```
frankfurt-latorre2-web/
├── .claude/memory/
│   ├── project.md
│   ├── session.md
│   └── history/
├── specs/
│   └── discovery.md
├── src/
│   ├── components/
│   ├── layouts/
│   ├── pages/
│   └── styles/
├── public/
│   └── images/
├── astro.config.mjs
├── package.json
└── CLAUDE.md
```

## Convencions

- **Components:** PascalCase (Hero.astro, ProductCard.astro)
- **Utilitats:** camelCase
- **CSS:** kebab-case per classes
- **Commits:** Conventional commits en català, sense emojis

---

## Flux de Treball IAvers-MemSys3

### Com Treballar amb Aquest Projecte

L'usuari pot parlar en llenguatge natural. Claude actuarà com a **orquestrador** i coordinarà tot el procés automàticament.

### Fases del Projecte

SCOUT (discovery) -> PLAN (roadmap) -> BUILD (implementar) -> VALIDATE (testing) -> SHIP (deploy)

### Estat Actual
- **Fase:** PLAN (pendent generar roadmap)
- **Pròxim pas:** Executar `/roadmap` o dir "genera el roadmap"

### Mode Orquestrador

Quan l'usuari diu coses com:
- "Comença a implementar el projecte"
- "Actua com a orquestrador"
- "Implementa tot el MVP"

Claude ha de:

1. **Verificar roadmap** - Si no existeix `specs/roadmap.md`, generar-lo primer
2. **Implementar fase per fase** - Seguir l'ordre, demanar confirmació en punts clau
3. **Gestionar Git** - Suggerir commits, mai push sense confirmació
4. **Usar subagents si eficient** - Per tasques independents, llançar en paral·lel

### Subagents Disponibles

| Agent | Quan Usar |
|-------|-----------|
| developer | Implementar codi |
| quality | Crear tests, validar |
| scout | Explorar codebase |

### Punts de Confirmació

L'orquestrador SEMPRE demana confirmació abans de:
- Començar una nova fase
- Fer canvis destructius
- Fer commit o push
- Decisions arquitectòniques importants

### Commands Disponibles

| Command | Descripció |
|---------|------------|
| `/roadmap` | Genera pla d'implementació complet |
| `/build [fase]` | Implementa una fase |
| `/commit` | Commit amb missatge suggerit |
| `/push` | Push amb validació |
| `/branch` | Gestió branques |
| `/status` | Estat del projecte |
| `/validate` | Verificar implementació |
| `/ship` | Preparar deploy |

### Regles de l'Orquestrador

1. **Sempre informar** què s'està fent
2. **Demanar confirmació** en punts crítics
3. **No assumir** - preguntar si hi ha dubtes
4. **Commits freqüents** - suggerir després de cada tasca significativa
5. **Actualitzar memòria** - registrar progrés a session.md

### Inici Ràpid

Per començar, simplement digues:

> "Genera el roadmap i després comença a implementar"
