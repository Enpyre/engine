from . import js_interface


def draw_canvas(x, y, color='#000000'):
    js_interface.drawCanvas(x, y, color)

def draw_circle(x, y, r, color='#000000'):
    js_interface.drawCircle(x, y, r, color)