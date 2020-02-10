#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.parameters import Button

# up/down buttons to change frequency
freq = 500
volume = 30

while True:
    buttons = brick.buttons()
    if Button.UP in buttons:
        freq += 10

    elif Button.DOWN in buttons:
        freq -= 10
    
    elif Button.LEFT in buttons:
        volume = max(0, volume-10)
    
    elif Button.RIGHT in buttons:
        volume = min(100, volume+10)

    brick.sound.beep(freq, 300, volume)
