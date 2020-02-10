#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.parameters import Button, Color

while True:
    b = brick.buttons()
    if Button.LEFT in b:
        brick.light(Color.GREEN)

    elif Button.CENTER in b:
        brick.light(Color.YELLOW)

    elif Button.RIGHT in b:
        brick.light(Color.RED)

    else:
        brick.light(None)
