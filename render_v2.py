RENDER_VERSION = "GA-V2-CLEAN-19"

from rules_v2 import show_description


def safe_bg_style(image_data: str, overlay_top: str, overlay_bottom: str, fallback_a: str, fallback_b: str) -> str:
    if image_data:
        return f"background-image: linear-gradient({overlay_top}, {overlay_bottom}), url('{image_data}');"
    return f"background: linear-gradient(135deg, {fallback_a} 0%, {fallback_b} 100%);"


def logo_html(logo_data: str) -> str:
    if not logo_data:
        return ""
    return f'<img src="{logo_data}" alt="El Periódico" class="brand-logo" />'


def build_post_html(
    title: str,
    description: str,
    image_data: str,
    section_label: str,
    family: str,
    logo_white_data: str,
    logo_green_data: str,
) -> str:
    title = (title or "").strip()
    description = (description or "").strip()

    if family == "general_b":
        return build_general_b(title, description, image_data, section_label, logo_green_data)
    if family == "deportes_a":
        return build_deportes_a(title, description, image_data, section_label, logo_white_data)
    if family == "deportes_b":
        return build_deportes_b(title, description, image_data, section_label, logo_green_data)
    if family == "policiales":
        return build_policiales(title, description, image_data, section_label, logo_white_data)
    return build_general_a(title, description, image_data, section_label, logo_white_data)


def global_styles() -> str:
    return """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Passion+One:wght@400;700;900&family=PT+Sans:wght@400;700&display=swap');

      * { box-sizing: border-box; }

      html, body {
        margin: 0;
        padding: 0;
        width: 1080px;
        height: 1350px;
        overflow: hidden;
        background: #111;
      }

      .canvas {
        width: 1080px;
        height: 1350px;
        position: relative;
        overflow: hidden;
        font-family: 'PT Sans', sans-serif;
      }

      .section-chip {
        position: absolute;
        top: 48px;
        left: 56px;
        padding: 12px 22px;
        border-radius: 999px;
        background: rgba(31, 139, 76, .34);
        border: 1px solid rgba(82, 188, 88, .52);
        color: #fff;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: .04em;
        text-transform: uppercase;
        z-index: 6;
        backdrop-filter: blur(4px);
      }

      .title {
        font-family: 'Passion One', sans-serif;
        font-weight: 400;
        line-height: 1.07;
        letter-spacing: 0;
        margin: 0;
      }

      .desc {
        margin: 18px 0 0 0;
        font-size: 25px;
        line-height: 1.34;
        font-weight: 700;
        max-width: 790px;
      }

      .brand-wrap-center {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        bottom: 50px;
        z-index: 7;
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }

      .brand-logo {
        display: block;
        width: 228px;
        height: auto;
      }

      .accent-bar-center {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        bottom: 28px;
        z-index: 7;
        border-radius: 2px;
      }
    </style>
    """


def build_general_a(title, description, image_data, section_label, logo_data) -> str:
    bg = safe_bg_style(
        image_data=image_data,
        overlay_top="rgba(0,0,0,.07)",
        overlay_bottom="rgba(10,40,20,.68)",
        fallback_a="#1a1f1b",
        fallback_b="#0f120f",
    )

    return f"""
    <html>
      <head>
        <meta charset="utf-8">
        {global_styles()}
        <style>
          .ga {{
            color: #fff;
            background-size: cover;
            background-position: center;
            {bg}
          }}

          .ga::after {{
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(
              to top,
              rgba(0,0,0,.08) 0%,
              rgba(0,0,0,0) 38%
            );
            z-index: 1;
            pointer-events: none;
          }}

          .ga .title-wrap {{
            position: absolute;
            left: 56px;
            right: 108px;
            bottom: 196px;
            z-index: 5;
          }}

          .ga .title {{
            font-size: 68px;
            max-width: 840px;
            text-shadow: 0 2px 7px rgba(0,0,0,.16);
          }}

          .ga .brand-logo {{
            width: 228px;
          }}

          .ga .accent-bar-center {{
            width: 190px;
            height: 10px;
            background: #2aa357;
          }}
        </style>
      </head>
      <body>
        <div class="canvas ga">
          <div class="section-chip">{section_label}</div>
          <div class="title-wrap">
            <h1 class="title">{title}</h1>
          </div>
          <div class="brand-wrap-center">{logo_html(logo_data)}</div>
          <div class="accent-bar-center"></div>
        </div>
      </body>
    </html>
    """


def build_general_b(title, description, image_data, section_label, logo_data) -> str:
    photo_style = f"background-image: url('{image_data}');" if image_data else "background: linear-gradient(135deg, #273126 0%, #1a2119 100%);"
    desc_html = f"<p class='desc'>{description}</p>" if show_description(description) else ""

    return f"""
    <html>
      <head>
        <meta charset="utf-8">
        {global_styles()}
        <style>
          .gb {{
            background: #f1efea;
            color: #111;
          }}

          .gb .photo {{
            position: absolute;
            top: 0;
            left: 0;
            width: 1080px;
            height: 780px;
            {photo_style}
            background-size: cover;
            background-position: center;
          }}

          .gb .photo::after {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(rgba(0,0,0,.02), rgba(0,0,0,.10));
          }}

          .gb .panel {{
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: 520px;
            background: #f1efea;
            padding: 46px 56px 34px 56px;
          }}

          .gb .bar {{
            position: absolute;
            left: 56px;
            top: 56px;
            width: 14px;
            height: 118px;
            background: #1f8b4c;
            border-radius: 2px;
          }}

          .gb .inner {{
            margin-left: 34px;
          }}

          .gb .section-chip-inline {{
            display: inline-block;
            padding: 10px 18px;
            border-radius: 999px;
            background: rgba(31, 139, 76, .16);
            border: 1px solid rgba(66, 171, 108, .34);
            color: #1f8b4c;
            font-size: 19px;
            font-weight: 700;
            letter-spacing: .04em;
            text-transform: uppercase;
            margin-bottom: 18px;
          }}

          .gb .title {{
            font-size: 58px;
            font-weight: 400;
            color: #111;
            max-width: 820px;
            line-height: 1.08;
          }}

          .gb .desc {{
            color: #3d3d3d;
            font-size: 25px;
            line-height: 1.34;
            max-width: 790px;
            margin-top: 18px;
          }}

          .gb .brand-wrap-center {{
            bottom: 38px;
          }}

          .gb .brand-logo {{
            width: 228px;
          }}

          .gb .accent-bar-center {{
            width: 138px;
            height: 7px;
            background: #1f8b4c;
          }}
        </style>
      </head>
      <body>
        <div class="canvas gb">
          <div class="photo"></div>
          <div class="panel">
            <div class="bar"></div>
            <div class="inner">
              <div class="section-chip-inline">{section_label}</div>
              <h1 class="title">{title}</h1>
              {desc_html}
            </div>
            <div class="brand-wrap-center">{logo_html(logo_data)}</div>
            <div class="accent-bar-center"></div>
          </div>
        </div>
      </body>
    </html>
    """


def build_highlight_html(raw_title: str) -> str:
    """
    Genera el HTML del título con banda de highlight naranja.
    Prioridad: dos puntos > patrón numérico > sin highlight.
    La banda cubre solo el fragmento resaltado, no borde a borde.
    """
    import re

    if ":" in raw_title:
        left, right = raw_title.split(":", 1)
        if left.strip():
            highlighted = f'<span class="hl-band">{left.strip()}:</span>'
            rest = right.strip()
            return f'{highlighted}<br>{rest}' if rest else highlighted

    numeric_patterns = [
        r'\b\d+\s*[-–a]\s*\d+\b',
        r'\bfecha\s+\d+\b',
        r'\bjornada\s+\d+\b',
        r'\b\d{{1,2}}:\d{{2}}\b',
    ]
    for pattern in numeric_patterns:
        match = re.search(pattern, raw_title, re.IGNORECASE)
        if match:
            start, end = match.span()
            before = raw_title[:start].strip()
            matched = raw_title[start:end].strip()
            after = raw_title[end:].strip()
            parts = []
            if before:
                parts.append(before)
            parts.append(f'<span class="hl-band">{matched}</span>')
            if after:
                parts.append(after)
            return " ".join(parts)

    return raw_title


def build_deportes_a(title, description, image_data, section_label, logo_data) -> str:
    """
    Deportes A: foto full con corte diagonal + zona naranja sólida abajo.
    Highlight de banda naranja en el fragmento correspondiente del título.
    """
    raw_title = (title or "").strip()
    title_html = build_highlight_html(raw_title)

    photo_style = f"background-image: url('{image_data}');" if image_data else "background: #1a1f1b;"

    return f"""
    <html>
      <head>
        <meta charset="utf-8">
        {global_styles()}
        <style>
          .depa {{
            background: #c96d2b;
            color: #fff;
            overflow: hidden;
          }}

          /* Foto con clip diagonal */
          .depa .photo {{
            position: absolute;
            top: 0;
            left: 0;
            width: 1080px;
            height: 900px;
            {photo_style}
            background-size: cover;
            background-position: center top;
            clip-path: polygon(0 0, 1080px 0, 1080px 780px, 0 900px);
            z-index: 1;
          }}

          /* Overlay oscuro sobre la foto */
          .depa .photo::after {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(
              to bottom,
              rgba(0,0,0,.08) 0%,
              rgba(0,0,0,.45) 100%
            );
          }}

          /* Zona naranja inferior */
          .depa .zona-naranja {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 560px;
            background: #c96d2b;
            z-index: 0;
          }}

          /* Contenedor del título */
          .depa .title-wrap {{
            position: absolute;
            left: 56px;
            right: 72px;
            bottom: 178px;
            z-index: 5;
          }}

          .depa .title {{
            font-size: 72px;
            line-height: 1.06;
            color: #fff;
            max-width: 920px;
          }}

          /* Banda de highlight: fondo naranja oscuro detrás del fragmento */
          .depa .hl-band {{
            display: inline;
            background: #fff;
            color: #c96d2b;
            padding: 0 8px;
            box-decoration-break: clone;
            -webkit-box-decoration-break: clone;
            border-radius: 3px;
          }}

          .depa .brand-logo {{
            width: 228px;
            filter: brightness(0) invert(1);
          }}

          .depa .accent-bar-center {
    display: none;
    }
        </style>
      </head>
      <body>
        <div class="canvas depa">
          <div class="zona-naranja"></div>
          <div class="photo"></div>
          <div class="title-wrap">
            <h1 class="title">{title_html}</h1>
          </div>
          <div class="brand-wrap-center">{logo_html(logo_data)}</div>
        </div>
      </body>
    </html>
    """


def build_deportes_b(title, description, image_data, section_label, logo_data) -> str:
    """
    Deportes B: variante sobria con panel claro y barra naranja.
    Sin highlight. Descripción condicional ≤ 150 chars.
    """
    photo_style = f"background-image: url('{image_data}');" if image_data else "background: linear-gradient(135deg, #273126 0%, #1a2119 100%);"
    desc_html = f"<p class='desc'>{description}</p>" if show_description(description) else ""

    return f"""
    <html>
      <head>
        <meta charset="utf-8">
        {global_styles()}
        <style>
          .depb {{
            background: #efede8;
            color: #111;
          }}

          .depb .photo {{
            position: absolute;
            top: 0;
            left: 0;
            width: 1080px;
            height: 760px;
            {photo_style}
            background-size: cover;
            background-position: center;
          }}

          .depb .photo::after {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(rgba(0,0,0,.03), rgba(0,0,0,.12));
          }}

          .depb .panel {{
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: 530px;
            background: #efede8;
            padding: 36px 56px 18px 56px;
          }}

          .depb .bar {{
            position: absolute;
            left: 56px;
            top: 44px;
            width: 14px;
            height: 128px;
            background: #c96d2b;
            border-radius: 2px;
          }}

          .depb .inner {{
            margin-left: 34px;
          }}

          .depb .section-chip-inline {{
            display: inline-block;
            padding: 10px 18px;
            border-radius: 999px;
            background: rgba(201, 109, 43, .14);
            border: 1px solid rgba(201, 109, 43, .38);
            color: #c96d2b;
            font-size: 19px;
            font-weight: 700;
            letter-spacing: .04em;
            text-transform: uppercase;
            margin-bottom: 18px;
          }}

          .depb .title {{
            font-size: 62px;
            font-weight: 400;
            color: #111;
            max-width: 860px;
            line-height: 1.08;
          }}

          .depb .desc {{
            color: #3d3d3d;
            font-size: 25px;
            line-height: 1.34;
            max-width: 790px;
            margin-top: 18px;
          }}

          .depb .brand-wrap-center {{
            bottom: 38px;
          }}

          .depb .brand-logo {{
            width: 228px;
          }}

          .depb .accent-bar-center {{
            width: 138px;
            height: 7px;
            background: #1f8b4c;
          }}
        </style>
      </head>
      <body>
        <div class="canvas depb">
          <div class="photo"></div>
          <div class="panel">
            <div class="bar"></div>
            <div class="inner">
              <div class="section-chip-inline">{section_label}</div>
              <h1 class="title">{title}</h1>
              {desc_html}
            </div>
            <div class="brand-wrap-center">{logo_html(logo_data)}</div>
            <div class="accent-bar-center"></div>
          </div>
        </div>
      </body>
    </html>
    """


def build_policiales(title, description, image_data, section_label, logo_data) -> str:
    """
    Policiales: foto full con overlay gris/negro puro, sin tinte de color de marca.
    """
    bg = safe_bg_style(
        image_data=image_data,
        overlay_top="rgba(0,0,0,.18)",
        overlay_bottom="rgba(0,0,0,.78)",
        fallback_a="#171717",
        fallback_b="#090909",
    )

    return f"""
    <html>
      <head>
        <meta charset="utf-8">
        {global_styles()}
        <style>
          .pol {{
            color: #fff;
            background-size: cover;
            background-position: center;
            {bg}
          }}

          .pol::after {{
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(
              to top,
              rgba(0,0,0,.10) 0%,
              rgba(0,0,0,0) 42%
            );
            z-index: 1;
            pointer-events: none;
          }}

          .pol .title-wrap {{
            position: absolute;
            left: 56px;
            right: 112px;
            bottom: 196px;
            z-index: 5;
          }}

          .pol .title {{
            font-size: 64px;
            max-width: 820px;
            text-shadow: 0 2px 7px rgba(0,0,0,.22);
          }}

          .pol .brand-logo {{
            width: 228px;
          }}

          .pol .accent-bar-center {{
            width: 142px;
            height: 6px;
            background: #ffffff;
            opacity: .85;
          }}
        </style>
      </head>
      <body>
        <div class="canvas pol">
          <div class="section-chip">{section_label}</div>
          <div class="title-wrap">
            <h1 class="title">{title}</h1>
          </div>
          <div class="brand-wrap-center">{logo_html(logo_data)}</div>
          <div class="accent-bar-center"></div>
        </div>
      </body>
    </html>
    """
