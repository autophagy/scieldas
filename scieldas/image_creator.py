import svgwrite
import cairosvg


def create_image(filetype, text_func, *func_params):
    if filetype not in ("svg", "png"):
        raise ValueError("{0} file type is not supported.")

    text = text_func(*func_params)
    height = 41
    # Width is our twice our padding (2*16) plus 7 pixels per character
    width = (len(text) * 7) + 32
    if filetype == "svg":
        return create_svg(text, height, width)
    if filetype == "png":
        return create_png(text, height, width)


def create_svg(text, height, width):

    svg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
    scield_rect = svg.rect(size=("100%", "100%"), fill="#2D2D2D")
    scield_text = svg.text(text, insert=(160, 240), fill="#F2F2F2")
    scield_text.update(
        {
            "font_family": "Inconsolata, Courier, monospace",
            "font_size": "140",
            "transform": "scale(.1)",
            "textLength": f"{(width*10)-(160*2)}",
        }
    )

    svg.add(scield_rect)
    svg.add(scield_text)
    return svg


def create_png(text, height, width):

    svg = create_svg(text, height, width)
    png = cairosvg.svg2png(
        bytestring=svg.tostring().encode(), parent_width=width, parent_height=height
    )
    return png
