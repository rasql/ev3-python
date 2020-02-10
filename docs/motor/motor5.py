#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button, Stop
from pybricks.tools import print, wait, StopWatch
import math

motor = Motor(Port.B)
watch = StopWatch()
amplitude = 90

while True:
    bts = brick.buttons()

    t = watch.time()/1000
    angle = math.sin(t) * amplitude
    motor.track_target(angle)
    
    if Button.CENTER in bts:
        break
