"""
Frankfurt La Torre 2 — Llista de cartells a generar.

Tipus:
  - Producte      → plats i menjar real
  - Temàtic       → personatges, monstres, humor
  - Estacional    → estiu, hivern, festes
  - Ambient/marca → atmosfera del local
"""
from brand import VISUAL_STYLE

# Estil visual compartit per cartells temàtics/humorístics
PULP_STYLE = (
    "vintage 1950s exploitation movie poster painted illustration, "
    "dramatic lighting, saturated colors, heavy film grain, "
    "pulp horror aesthetic, no text, no letters, illustration only"
)

JOBS = [

    # ════════════════════════════════════════════
    # PRODUCTES
    # ════════════════════════════════════════════

    {
        "file":    "promo_frankfurt_classic.jpg",
        "prompt": (
            "close-up of a perfectly grilled frankfurt sausage in a fresh bread roll, "
            "mustard drizzle, crispy edges, steam rising, dark wooden board, "
            + VISUAL_STYLE
        ),
        "palette":      "frankfurt_orange",
        "kicker":       "L'ORIGINAL DES DE SEMPRE",
        "title_top":    "FRANKFURT",
        "title_bottom": "LA TORRE 2",
        "tagline":      "Pineda de Mar. Cada dia.",
    },
    {
        "file":    "promo_burguer.jpg",
        "prompt": (
            "juicy gourmet burger with melted cheese, fresh lettuce, tomato, "
            "sesame bun, dramatic side view, dark moody background, "
            + VISUAL_STYLE
        ),
        "palette":      "frankfurt_orange",
        "kicker":       "FET A MÀ · CADA DIA",
        "title_top":    "LA BURGUER",
        "title_bottom": "DE PINEDA",
        "tagline":      "Carn fresca. Sense excuses.",
    },
    {
        "file":    "promo_bratwurst.jpg",
        "prompt": (
            "grilled German bratwurst sausage on a rustic plate, "
            "golden grill marks, herbs, warm summer light, "
            + VISUAL_STYLE
        ),
        "palette":      "frankfurt_night",
        "kicker":       "DIRECTE DE LA PLANXA",
        "title_top":    "BRATWURST",
        "title_bottom": "A LA BRASA",
        "tagline":      "L'autèntic sabor alemany.",
    },
    {
        "file":    "promo_braves.jpg",
        "prompt": (
            "crispy golden patatas bravas with spicy tomato sauce and aioli, "
            "top-down view, rustic terracotta bowl, warm light, "
            + VISUAL_STYLE
        ),
        "palette":      "frankfurt_light",
        "kicker":       "LES MILLORS DE PINEDA",
        "title_top":    "PATATES",
        "title_bottom": "BRAVES",
        "tagline":      "Crispetes. Salsa. Punt.",
    },

    # ════════════════════════════════════════════
    # TEMÀTICS / HUMORÍSTICS
    # ════════════════════════════════════════════

    {
        "file":    "tema_homellop.jpg",
        "prompt": (
            "vintage 1941 Wolf Man movie poster painted illustration, "
            "werewolf with hairy face, wolf snout and fangs, torn shirt, "
            "sitting hunched at a restaurant table, holding a frankfurt sausage, "
            "looking hungry and menacing, gothic atmosphere, full moon outside window, "
            + PULP_STYLE
        ),
        "palette":      "frankfurt_night",
        "kicker":       "OBERT FINS QUE SURT LA LLUNA",
        "title_top":    "L'HOME LLOP",
        "title_bottom": "TÉ GANA",
        "tagline":      "Frankfurt La Torre 2. Fins tard.",
    },
    {
        "file":    "tema_dracula.jpg",
        "prompt": (
            "vintage 1931 Dracula movie poster painted illustration, "
            "Count Dracula in black cape, pale skin, fangs bared, "
            "sitting at a restaurant table with a plate of sausages, "
            "red glowing eyes, gothic candelabra, castle dining room, "
            + PULP_STYLE
        ),
        "palette":      "frankfurt_night",
        "kicker":       "NECESSITA PROTEÏNES",
        "title_top":    "DRÀCULA",
        "title_bottom": "HA SOPAT",
        "tagline":      "Oberts cada nit. Frankfurt La Torre 2.",
    },
    {
        "file":    "tema_frankenstein.jpg",
        "prompt": (
            "vintage 1931 Frankenstein monster movie poster painted illustration, "
            "Frankenstein's monster with flat head and neck bolts, "
            "wearing a striped restaurant apron, holding a giant frankfurt sausage, "
            "friendly but menacing expression, dramatic lightning background, "
            + PULP_STYLE
        ),
        "palette":      "frankfurt_orange",
        "kicker":       "FET A MÀ (LITERALMENT)",
        "title_top":    "FRANKENSTEIN",
        "title_bottom": "CUINA",
        "tagline":      "El monstre sap cuinar. Vine a provar-ho.",
    },
    {
        "file":    "tema_momia.jpg",
        "prompt": (
            "vintage 1932 mummy horror movie poster painted illustration, "
            "Egyptian mummy wrapped in dusty bandages, "
            "queuing at a fast food counter, arms outstretched forward, "
            "looking at a menu board, ancient meets modern comedy, "
            + PULP_STYLE
        ),
        "palette":      "frankfurt_orange",
        "kicker":       "5.000 ANYS ESPERANT",
        "title_top":    "LA MÒMIA",
        "title_bottom": "FA CUA",
        "tagline":      "Val la pena esperar. Frankfurt La Torre 2.",
    },

    # ════════════════════════════════════════════
    # ESTACIONAL
    # ════════════════════════════════════════════

    {
        "file":    "promo_estiu.jpg",
        "prompt": (
            "vibrant summer beach scene with a food stall, "
            "grilled sausages and burgers, Mediterranean coast, "
            "sunny day, happy summer atmosphere, "
            + VISUAL_STYLE
        ),
        "palette":      "frankfurt_orange",
        "kicker":       "TEMPORADA D'ESTIU 2026",
        "title_top":    "OBERTS",
        "title_bottom": "FINS TARD",
        "tagline":      "De les 12h fins tancar. A punt per tu.",
    },

    # ════════════════════════════════════════════
    # AMBIENT / MARCA (Stories verticals)
    # ════════════════════════════════════════════

    {
        "file":    "story_nit.jpg",
        "prompt": (
            "cozy street food restaurant at night, warm orange lights, "
            "people eating at outdoor tables, Mediterranean town square, "
            "inviting summer evening atmosphere, "
            + VISUAL_STYLE
        ),
        "palette":      "frankfurt_night",
        "size":         (1080, 1920),
        "kicker":       "OBERTS CADA NIT",
        "title_top":    "FRANKFURT",
        "title_bottom": "LA TORRE 2",
        "tagline":      "On acabar el dia.",
        "show_stars":   False,
    },
    {
        "file":    "story_homellop.jpg",
        "prompt": (
            "dark night forest with full moon, menacing werewolf silhouette "
            "running toward a warm glowing restaurant in the distance, "
            "dramatic horror movie atmosphere, "
            + PULP_STYLE
        ),
        "palette":      "frankfurt_night",
        "size":         (1080, 1920),
        "kicker":       "CAP ON VAS TAN DE PRESSA?",
        "title_top":    "L'HOME LLOP",
        "title_bottom": "SAPS ON VA",
        "tagline":      "Frankfurt La Torre 2. Oberts fins tard.",
        "show_stars":   False,
    },
]
