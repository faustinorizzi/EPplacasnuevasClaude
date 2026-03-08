import re
from urllib.parse import urlparse

MAX_DESCRIPTION_CHARS = 150


def infer_section_from_url(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if not path:
        return "general"

    first = path.split("/")[0].lower()

    mapping = {
        "local": "general",
        "region": "general",
        "el-pais": "general",
        "mundo": "general",
        "motor": "general",
        "tecnologia": "general",
        "educacion": "general",
        "negocios": "general",
        "salud": "general",
        "deportes": "deportes",
        "policiales": "policiales",
        "espectaculos": "general_b",
    }

    return mapping.get(first, "general")


def display_section_label(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if not path:
        return "GENERAL"

    first = path.split("/")[0].lower()

    labels = {
        "local": "LOCAL",
        "region": "REGIÓN",
        "el-pais": "EL PAÍS",
        "mundo": "MUNDO",
        "motor": "MOTOR",
        "tecnologia": "TECNOLOGÍA",
        "educacion": "EDUCACIÓN",
        "negocios": "NEGOCIOS",
        "salud": "SALUD",
        "deportes": "DEPORTES",
        "policiales": "POLICIALES",
        "espectaculos": "ESPECTÁCULOS",
    }

    return labels.get(first, "GENERAL")


def has_numeric_pattern(title: str) -> bool:
    """Detecta marcadores, fechas o números destacables en el título."""
    patterns = [
        r'\b\d+\s*[-–a]\s*\d+\b',   # marcadores: 3-1, 2-0, 76-72
        r'\bfecha\s+\d+\b',           # fecha 10, fecha 5
        r'\bjornada\s+\d+\b',         # jornada 3
        r'\bfecha\b.*\d+',            # fecha + número
        r'\b\d{1,2}:\d{2}\b',         # horarios tipo 20:00
    ]
    title_lower = title.lower()
    return any(re.search(p, title_lower) for p in patterns)


def choose_deportes_variant(title: str) -> str:
    """Elige entre deportes_a (highlight) y deportes_b (panel sobrio)."""
    title = (title or "").strip()
    if ":" in title:
        left = title.split(":")[0].strip()
        if left:
            return "deportes_a"
    if has_numeric_pattern(title):
        return "deportes_a"
    return "deportes_b"


def show_description(description: str) -> bool:
    """Muestra descripción solo si no supera el máximo de caracteres."""
    if not description:
        return False
    return len(description.strip()) <= MAX_DESCRIPTION_CHARS


def choose_family(section: str, title: str, description: str) -> str:
    title = (title or "").strip()
    description = (description or "").strip().lower()

    if section == "deportes":
        return choose_deportes_variant(title)

    if section == "policiales":
        return "policiales"

    if section == "general_b":
        return "general_b"

    keywords = [
        "invitan",
        "charla",
        "curso",
        "capacitación",
        "capacitacion",
        "cortes",
        "cronograma",
        "inscripciones",
        "gratuita",
        "gratuito",
        "requisitos",
        "agenda",
    ]

    title_long = len(title) >= 95
    desc_present = len(description) >= 80
    has_keyword = any(k in description or k in title.lower() for k in keywords)

    if (title_long and has_keyword) or (has_keyword and desc_present):
        return "general_b"

    return "general_a"
