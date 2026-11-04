"""
Frankfurt La Torre 2 — Llançador de cartells.

Ús:
  python3 run.py                        # Genera tots els cartells
  python3 run.py burguer braves         # Genera només els que contenen "burguer" o "braves"
  python3 run.py --list                 # Mostra els cartells disponibles

Requeriments:
  pip3 install Pillow
"""
from __future__ import annotations

import asyncio
import os
import sys
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from brand import LOGO_PATH, MASCOT_PATH, PALETTES, FONT_HEADING, FONT_BODY, FOOTER_LEFT, FOOTER_RIGHT
from jobs import JOBS

ROOT   = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
CACHE  = ROOT / "cache"
OUTPUT.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(parents=True, exist_ok=True)

# ── Fons ──────────────────────────────────────────────────────────────────────
# Fins al 27/08/2026 aquí es cridava `api.freepik.com` amb FREEPIK_API_KEY.
# Aquella clau va acabar commitada al repo de llull-v3 i encara és a la seva
# història de git, o sigui que s'havia de retirar.
#
# La substituta d'IAvers per a generació visual és Magnific, i Magnific NO és
# una API amb clau: és un MCP amb OAuth de claude.ai. Un script autònom no la
# pot cridar. Per tant això ja no genera imatges: les CONSUMEIX. Qui les genera
# és una sessió de Claude amb Magnific, que les deixa a `cache/`.
#
# Propietat nova i volguda: un cop generat un fons, el cartell es pot refer
# infinites vegades sense xarxa, sense claus i sense ningú.

CACHE_ENTRADA = CACHE / "pendents"
EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


class FonsAbsent(RuntimeError):
    """Falta la imatge de fons. Un error que no diu com sortir-ne és mig error."""

    def __init__(self, clau: str, desti: Path):
        self.clau, self.desti = clau, desti
        super().__init__(
            f"falta el fons «{clau}». Genera'l amb Magnific i desa'l a {desti}"
        )


def _normalitza(origen: Path, desti: Path) -> bytes:
    """Magnific torna PNG o WebP segons el model; la resta del pipeline vol JPEG."""
    with Image.open(origen) as img:
        img.convert("RGB").save(desti, "JPEG", quality=92)
    return desti.read_bytes()


async def get_bg_cached(cache_key: str, prompt: str, aspect: str = "square_1_1") -> bytes:
    fitxer = CACHE / f"{cache_key}.jpg"
    if fitxer.exists():
        print(f"  (cache hit: {cache_key})")
        return fitxer.read_bytes()

    # Safata d'entrada: qualsevol imatge deixada a cache/pendents/ amb el nom
    # de la clau s'adopta sola. És el camí que fa servir una sessió de Claude.
    if CACHE_ENTRADA.is_dir():
        for ext in EXTENSIONS:
            candidat = CACHE_ENTRADA / f"{cache_key}{ext}"
            if candidat.exists():
                dades = _normalitza(candidat, fitxer)
                candidat.unlink()
                print(f"  (fons adoptat de pendents/: {cache_key})")
                return dades

    # El prompt es deixa al costat d'on ha d'anar la imatge: així no cal
    # tornar-lo a buscar al jobs.py per generar-la.
    fitxer.with_suffix(".prompt.txt").write_text(
        f"# Fons pendent: {cache_key}\n"
        f"# Genera'l amb Magnific i desa'l a: {fitxer}\n"
        f"# (o deixa'l a {CACHE_ENTRADA}/{cache_key}.png i s'adoptarà sol)\n"
        f"# aspect: {aspect}\n\n{prompt}\n",
        encoding="utf-8",
    )
    raise FonsAbsent(cache_key, fitxer)


# ── Composició ────────────────────────────────────────────────────────────────

def add_grain(img: Image.Image, intensity: int = 30) -> Image.Image:
    noise = Image.effect_noise(img.size, intensity).convert("RGB")
    return Image.blend(img, noise, 0.06)


def fit_text(draw, text: str, font_path: str, max_width: int, max_size: int) -> ImageFont.FreeTypeFont:
    size = max_size
    while size > 10:
        font = ImageFont.truetype(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            return font
        size -= 4
    return ImageFont.truetype(font_path, size)


def compose_poster(
    bg_bytes: bytes,
    size: tuple[int, int],
    palette: dict,
    kicker: str,
    title_top: str,
    title_bottom: str,
    tagline: str,
    show_stars: bool = True,
) -> Image.Image:
    w, h = size

    # Fons
    bg = Image.open(BytesIO(bg_bytes)).convert("RGB").resize(size, Image.LANCZOS)
    bg = add_grain(bg, 35)
    wash = Image.new("RGB", size, palette["bg"])
    bg = Image.blend(bg, wash, 0.15)
    canvas = bg.convert("RGBA")
    draw = ImageDraw.Draw(canvas)

    # Bandes superiors i inferiors
    band_h = int(h * 0.055)
    draw.rectangle([0, 0, w, band_h], fill=palette["fg"])
    draw.rectangle([0, h - band_h, w, h], fill=palette["fg"])

    # Kicker a la banda superior
    kicker_font = ImageFont.truetype(FONT_HEADING, int(h * 0.026))
    kicker_y = (band_h - int(h * 0.026)) // 2
    draw.text((int(w * 0.05), kicker_y), kicker, fill=palette["bg"], font=kicker_font)

    # Logo a la banda superior (cantonada dreta)
    logo_src = MASCOT_PATH if MASCOT_PATH.exists() else LOGO_PATH
    if logo_src.exists():
        logo = Image.open(logo_src).convert("RGBA")
        target_h = int(band_h * 0.90)
        ratio = target_h / logo.height
        target_w = int(logo.width * ratio)
        logo = logo.resize((target_w, target_h), Image.LANCZOS)
        lx = w - target_w - int(w * 0.03)
        ly = (band_h - target_h) // 2
        canvas.paste(logo, (lx, ly), logo)

    # Títols
    max_tw = int(w * 0.82)
    font_top = fit_text(draw, title_top, FONT_HEADING, max_tw, int(h * 0.20))
    font_bot = fit_text(draw, title_bottom, FONT_HEADING, max_tw, int(h * 0.20))
    tb_top = draw.textbbox((0, 0), title_top, font=font_top)
    tb_bot = draw.textbbox((0, 0), title_bottom, font=font_bot)
    top_w, top_h = tb_top[2] - tb_top[0], tb_top[3] - tb_top[1]
    bot_w, bot_h = tb_bot[2] - tb_bot[0], tb_bot[3] - tb_bot[1]

    center_y  = int(h * 0.44)
    pad       = int(h * 0.015)

    # Bloc títol superior
    tx = (w - top_w) // 2
    draw.rectangle([tx - pad * 2, center_y - pad, tx + top_w + pad * 2, center_y + top_h + pad], fill=palette["bg"])
    draw.text((tx, center_y - pad // 2), title_top, fill=palette["fg"], font=font_top)

    # Bloc títol inferior (accent)
    center_y2 = center_y + top_h + pad * 3
    bx = (w - bot_w) // 2
    draw.rectangle([bx - pad * 2, center_y2 - pad, bx + bot_w + pad * 2, center_y2 + bot_h + pad], fill=palette["accent"])
    draw.text((bx, center_y2 - pad // 2), title_bottom, fill=palette["bg"] if palette["bg"] != "#FFF9F5" else "#FFFFFF", font=font_bot)

    # Tagline
    tag_font = fit_text(draw, tagline, FONT_BODY, int(w * 0.9), int(h * 0.036))
    tag_y = center_y2 + bot_h + pad * 4
    draw.text((w // 2, tag_y), tagline, fill=palette["fg"], font=tag_font, anchor="mt")

    # Stars row (opcional)
    if show_stars:
        star_text = f"★ ★ ★  {FOOTER_LEFT}  ★ ★ ★"
        star_font = ImageFont.truetype(FONT_HEADING, int(h * 0.038))
        star_y = int(h * 0.13)
        tb = draw.textbbox((w // 2, star_y), star_text, font=star_font, anchor="mt")
        px, py = int(w * 0.03), int(h * 0.01)
        draw.rectangle([tb[0] - px, tb[1] - py, tb[2] + px, tb[3] + py], fill=palette["fg"])
        draw.text((w // 2, star_y), star_text, fill=palette["bg"], font=star_font, anchor="mt")

    # Footer
    foot_font = ImageFont.truetype(FONT_HEADING, int(h * 0.026))
    foot_y = h - band_h + int(band_h * 0.25)
    draw.text((int(w * 0.05), foot_y), FOOTER_LEFT, fill=palette["bg"], font=foot_font)
    draw.text((w - int(w * 0.05), foot_y), FOOTER_RIGHT, fill=palette["bg"], font=foot_font, anchor="rt")

    return canvas.convert("RGB")


# ── Main ──────────────────────────────────────────────────────────────────────

async def generate_batch(only: list[str] | None = None) -> list["FonsAbsent"]:
    pendents: list[FonsAbsent] = []
    for job in JOBS:
        if only and not any(k in job["file"] for k in only):
            continue

        size        = job.get("size", (1080, 1080))
        show_stars  = job.get("show_stars", True)
        aspect      = "square_1_1" if size == (1080, 1080) else "social_story_9_16"
        palette     = PALETTES[job["palette"]]
        cache_key   = job["file"].replace(".jpg", "")

        print(f"→ Generant {job['title_top']} {job['title_bottom']}...")
        try:
            bg_bytes = await get_bg_cached(cache_key, job["prompt"], aspect=aspect)
        except FonsAbsent as absent:
            # Un fons que falta no atura la tanda: si petés al primer, generar
            # 20 cartells nous voldria dir 20 execucions descobrint-ne un cada
            # cop. Així una sola passada et diu tot el que has de generar.
            print(f"  ⏸ falta el fons ({cache_key})")
            pendents.append(absent)
            continue
        poster = compose_poster(
            bg_bytes=bg_bytes,
            size=size,
            palette=palette,
            kicker=job["kicker"],
            title_top=job["title_top"],
            title_bottom=job["title_bottom"],
            tagline=job["tagline"],
            show_stars=show_stars,
        )
        out = OUTPUT / job["file"]
        poster.save(out, "JPEG", quality=92)
        print(f"  ✓ {out}")

    if pendents:
        print(f"\n⏸ {len(pendents)} fons per generar amb Magnific:")
        for p in pendents:
            print(f"   · {p.clau}  →  {p.desti}")
        print(
            "\n   Els prompts són als .prompt.txt del costat. Un cop hi siguin les "
            "imatges,\n   torna a executar-ho i es compondran sense tocar cap xarxa."
        )
    return pendents


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--list" in args:
        print("Cartells disponibles:")
        for j in JOBS:
            print(f"  · {j['file']}  [{j['palette']}]  — {j['title_top']} {j['title_bottom']}")
        sys.exit(0)
    only = args if args else None
    asyncio.run(generate_batch(only))
