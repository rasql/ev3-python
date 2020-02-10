#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from ev3dev2.sound import Sound

sound = Sound()
sound.speak('Welcome to the E V 3 dev project')

brick.display.text('Hello', (50, 50))
brick.display.text('World')

brick.sound.beep()

# Make the light red
brick.light(Color.RED)

motor1 = Motor(Port.B)
motor1.run_target(100, 360)
brick.sound.beep(1000, 500)

# Make the light red
brick.light(Color.GREEN)

brick.display.image(ImageFile.UP)
motor1.run_target(-1000, 0)

# Make 5 simple beeps
brick.sound.beeps(5)





brick.sound.file(SoundFile.HELLO)



