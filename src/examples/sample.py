from src.engine import pyongine



def update(time: float):
    if not hasattr(pyongine, 'circle'):
        pyongine.circle = pyongine.draw_circle(1+time, 1+time, 100, '#ffffff')
    else:
        pyongine.circle.x = 1+time
        pyongine.circle.y = 1+time

pyongine.run(800, 800, '#000000', update)
