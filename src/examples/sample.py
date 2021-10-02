from src.engine import pyongine


def update(time: float):
    x = y = time%800
    if not hasattr(pyongine, 'circle'):
        pyongine.circle = pyongine.draw_circle(x, y, 100, '#ffffff')
    else:
        pyongine.circle.x = x
        pyongine.circle.y = y

pyongine.run(800, 800, '#000000', update)


def update(time: float):
    SPEED = 3
    if not hasattr(pyongine, 'circle'):
        pyongine.circle = pyongine.draw_circle(100, 100, 100, '#ffffff')
    else:
        if pyongine.key_pressed(pyongine.KEY_UP):
            pyongine.circle.y -= SPEED
        if pyongine.key_pressed(pyongine.KEY_DOWN):
            pyongine.circle.y += SPEED
        if pyongine.key_pressed(pyongine.KEY_LEFT):
            pyongine.circle.x -= SPEED
        if pyongine.key_pressed(pyongine.KEY_RIGHT):
            pyongine.circle.x += SPEED

pyongine.run(400, 400, '#000000', update)
