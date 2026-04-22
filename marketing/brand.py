"""
Frankfurt La Torre 2 — Manifest de marca per al generador de cartells.

Colors extrets de: src/styles/global.css
Logo: public/logo1Web.png
Ninot: public/ninotfrankfurtWeb.png
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ── Logos ─────────────────────────────────────────────────────────────────────
LOGO_PATH       = PROJECT_ROOT / "public" / "logo1Web.png"
MASCOT_PATH     = PROJECT_ROOT / "public" / "ninotfrankfurtWeb.png"

# ── Paletes corporatives ──────────────────────────────────────────────────────
PALETTES = {
    # Principal: taronja corporatiu + fosc (cartells estiu/dia)
    "frankfurt_orange": {
        "bg":     "#E85A1B",   # taronja corporatiu
        "fg":     "#1A1A1A",   # fosc
        "accent": "#1E3A5F",   # blau marí
    },
    # Versió nocturna: blau marí + crema càlid (cartells nit/tardor)
    "frankfurt_night": {
        "bg":     "#1E3A5F",   # blau marí corporatiu
        "fg":     "#FFF9F5",   # crema càlid
        "accent": "#E85A1B",   # taronja
    },
    # Versió lleugera (stories, formats clars)
    "frankfurt_light": {
        "bg":     "#FFF9F5",   # crema càlid
        "fg":     "#1A1A1A",   # fosc
        "accent": "#E85A1B",   # taronja
    },
}

# ── Tipografia ────────────────────────────────────────────────────────────────
# Archivo Black és web font — usem Impact com a fallback disponible al sistema
# Per resultats òptims: instalar Archivo Black a ~/Library/Fonts/
FONT_HEADING = "/System/Library/Fonts/Supplemental/Impact.ttf"       # fallback
FONT_BODY    = "/System/Library/Fonts/Supplemental/Futura.ttc"

# ── Textos fixos de marca ─────────────────────────────────────────────────────
FOOTER_LEFT  = "PINEDA DE MAR"
FOOTER_RIGHT = "@FRANKFURT_LATORRE2"
BRAND_TAG    = "FRANKFURT LA TORRE 2"

# ── Estil de prompt Freepik (context visual) ──────────────────────────────────
VISUAL_STYLE = (
    "vibrant food photography poster art, warm saturated colors, "
    "street food market aesthetic, bold graphic design, "
    "appetizing close-up with dramatic lighting, "
    "Mediterranean summer feel, no text, no letters, illustration only"
)
