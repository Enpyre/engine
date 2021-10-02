from src.engine import pyongine

def update(time: float):
    pyongine.draw_circle(1+time, 1+time, 100, 0xffffff)

pyongine.run(800, 800, '#000000', update)
