"""
Frankfurt La Torre 2 — Llançador de cartells.

Ús:
  python3 run.py                        # Genera tots els cartells
  python3 run.py burguer braves         # Genera només els que contenen "burguer" o "braves"
  python3 run.py --list                 # Mostra els cartells disponibles

Requeriments:
  pip3 install httpx Pillow
  export FREEPIK_API_KEY=...
"""
from __future__ import annotations

import asyncio
import base64
import os
import sys
from io import BytesIO
from pathlib import Path

import httpx
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from brand import LOGO_PATH, MASCOT_PATH, PALETTES, FONT_HEADING, FONT_BODY, FOOTER_LEFT, FOOTER_RIGHT
from jobs import JOBS

ROOT   = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
CACHE  = ROOT / "cache"
OUTPUT.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(parents=True, exist_ok=True)

FREEPIK_ENDPOINT = "https://api.freepik.com/v1/ai/text-to-image"


# ── Freepik ───────────────────────────────────────────────────────────────────

async def freepik_flux(prompt: str, aspect: str = "square_1_1") -> bytes:
    api_key = os.environ.get("FREEPIK_API_KEY")
    if not api_key:
        raise RuntimeError("FREEPIK_API_KEY no definida.")
    payload = {"prompt": prompt, "num_images": 1, "image": {"size": aspect}}
    headers = {"Content-Type": "application/json", "x-freepik-api-key": api_key}
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(FREEPIK_ENDPOINT, headers=headers, json=payload)
        if resp.status_code != 200:
            raise RuntimeError(f"Freepik error {resp.status_code}: {resp.text[:400]}")
        data   = resp.json()
        images = data.get("data") or []
        if not images:
            raise RuntimeError(f"Cap imatge rebuda: {str(data)[:400]}")
        first = images[0]
        if first.get("base64"):
            return base64.b64decode(first["base64"])
        if first.get("url"):
            img_resp = await client.get(first["url"])
            return img_resp.content
        raise RuntimeError(f"Format no reconegut: {str(first)[:200]}")


async def get_bg_cached(cache_key: str, prompt: str, aspect: str = "square_1_1") -> bytes:
    cache_file = CACHE / f"{cache_key}.jpg"
    if cache_file.exists():
        print(f"  (cache hit: {cache_key})")
        return cache_file.read_bytes()
    bg_bytes = await freepik_flux(prompt, aspect=aspect)
    cache_file.write_bytes(bg_bytes)
    return bg_bytes


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

async def generate_batch(only: list[str] | None = None) -> None:
    for job in JOBS:
        if only and not any(k in job["file"] for k in only):
            continue

        size        = job.get("size", (1080, 1080))
        show_stars  = job.get("show_stars", True)
        aspect      = "square_1_1" if size == (1080, 1080) else "social_story_9_16"
        palette     = PALETTES[job["palette"]]
        cache_key   = job["file"].replace(".jpg", "")

        print(f"→ Generant {job['title_top']} {job['title_bottom']}...")
        bg_bytes = await get_bg_cached(cache_key, job["prompt"], aspect=aspect)
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


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--list" in args:
        print("Cartells disponibles:")
        for j in JOBS:
            print(f"  · {j['file']}  [{j['palette']}]  — {j['title_top']} {j['title_bottom']}")
        sys.exit(0)
    only = args if args else None
    asyncio.run(generate_batch(only))
