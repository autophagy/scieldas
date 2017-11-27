import svgwrite
import wand.image

def create_svg(text_func, *func_params):

    # Create the text

    text = text_func(*func_params)

    # Width is our twice our padding (2*16) plus 7 pixels per character
    svg = svgwrite.Drawing(size = ("{}px".format((len(text)*7)+32), "41px"))
    text_style = ("font-size: 14px; "
                  "font-family: Inconsolata, monospace;"
                  "text-align: center")
    scield_rect = svg.rect(size=('100%', '100%'), fill='#2D2D2D')
    scield_text = svg.text(text, insert=(16, 24), fill="#F2F2F2", style=text_style)

    svg.defs.add(svg.style("@import url('https://fonts.googleapis.com/css?family=Inconsolata');"))

    svg.add(scield_rect)
    svg.add(scield_text)
    return svg

def create_png(text_func, *func_params):

    svg = create_svg(text_func, *func_params)

    with wand.image.Image(blob=svg.tostring().encode(), format="svg") as image:
        png_image = image.make_blob("png")
    return png_image
