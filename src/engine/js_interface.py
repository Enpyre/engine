from typing import Callable


def drawCanvas(
    height: int,
    width: int,
    color: str,
    callback: Callable[[float], None]
):
    import js
    js.drawCanvas(height, width, color, callback)


def drawCircle(x: int, y: int, r: int, color: str):
    import js
    js.drawCircle(x, y, r, color)
