from typing import Callable
from .core import Core
from .graphics import Graphics

class Pyongine(Core, Graphics):
    KEY_UP = 'ArrowUp'
    KEY_LEFT = 'ArrowLeft'
    KEY_DOWN = 'ArrowDown'
    KEY_RIGHT = 'ArrowRight'

    def __init__(self):
        self.elapsed = 0.0
        Core.__init__(self)
        Graphics.__init__(self)

    def run(
        self,
        height: int,
        width: int,
        color: str,
        update: Callable[[float], None],
    ):
        self.elapsed = 0.0
        self.__update = update
        self.draw_canvas(height, width, color, self.update)

    def update(self, delta: float):
        self.elapsed += delta
        self.__update(self.elapsed)
