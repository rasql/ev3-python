#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button, Stop
from pybricks.tools import print, wait

motor = Motor(Port.B)

while True:
    bts = brick.buttons()
    if Button.RIGHT in bts:
        motor.run_angle(200, 500, Stop.COAST, False)

    elif Button.CENTER in bts:
        break

    print(motor.speed(), motor.angle())
    wait(100)
