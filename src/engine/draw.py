from . import js_interface


def draw_canvas(x, y):
    js_interface.drawCanvas(x, y)

def draw_circle(x, y, r, color):
    js_interface.drawCircle(x, y, r, color)