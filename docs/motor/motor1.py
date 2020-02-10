#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button
from pybricks.tools import print, wait

motor = Motor(Port.B)
cycle = 50

while True:
    bts = brick.buttons()
    if Button.LEFT in bts:
        cycle = max(-100, cycle-10)

    elif Button.RIGHT in bts:
        cycle = min(100, cycle+10)

    elif Button.CENTER in bts:
        break

    motor.dc(cycle)
    print(cycle, motor.speed(), motor.angle())
    wait(100)

