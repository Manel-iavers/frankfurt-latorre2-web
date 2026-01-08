# Discovery: Frankfurt la Torre 2 - Web

Data: 2026-01-08

## Visió
Landing page moderna per Frankfurt la Torre 2 (Pineda de Mar) amb integració SmartMenu Agora per gestionar comandes online amb recollida al local.

## Usuaris
Clients del restaurant que volen:
- Veure la carta i productes destacats
- Fer comandes per recollir
- Trobar ubicació i contacte

## Funcionalitats MVP

### Landing Page
- Hero amb CTA "Fer Comanda" ben visible
- Secció productes estrella (6 destacats)
- Secció "Nosaltres" (producte local)
- Ubicació + mapa + contacte
- Footer amb xarxes socials
- Botó flotant CTA sempre visible

### Sistema de Comandes
- Botó obre SmartMenu d'Agora (link extern)
- SmartMenu gestiona: catàleg, carret, client, comanda
- Pagament al recollir (no online)
- Impressió automàtica a cuina

## Requisits Tècnics
- No backend propi (SmartMenu Agora gestiona tot)
- Responsive/mobile-first
- Ràpid de carregar (Astro genera HTML estàtic)
- SEO optimitzat

## Decisions Stack
- **Framework:** Astro
  - Components reutilitzables
  - Fàcil escalar si cal afegir més pàgines
  - Zero JS per defecte (ràpid)
- **Backend:** Cap - SmartMenu Agora extern
- **Deploy:** Vercel o Netlify (recomanat)

## Disseny
- **Colors:**
  - Groc mostassa: #E8A936
  - Vermell: #C41E3A
  - Negre: #1A1A1A
  - Crema: #FFF8E7
- **Fonts:**
  - Títols: Archivo Black
  - Cos: DM Sans
- **Estil:** Modern, càlid, orientat a menjar

## Context Addicional
- URL actual: https://sites.google.com/view/frankfurtlatorre2/carta
- Fitxers referència: Guia_del_Integrador.pdf (API Agora)
- Prototip HTML creat en sessió anterior

## Pendent del Client
- [ ] URL SmartMenu (necessita ID establiment)
- [ ] Fotos reals productes
- [ ] Coordenades exactes mapa
- [ ] Horaris

---

## Pròxims Passos
1. [ ] Crear pla detallat amb `/roadmap`
2. [ ] Configurar projecte Astro
3. [ ] Implementar landing amb placeholders
4. [ ] Integrar SmartMenu quan tinguem URL
