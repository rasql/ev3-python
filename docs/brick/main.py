#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

print(Button)
print(Button.LEFT)
print(Button.RIGHT)
print(Button.UP)
print(Button.DOWN)



# print the list of pressed buttons to the remote console
# while True:
#     print(brick.buttons())
#     wait(300)

# button left=RED, right=GREEN 
# while True:
#     b = brick.buttons()
#     if Button.LEFT in b:
#         brick.light(Color.RED)
#     elif Button.RIGHT in b:
#         brick.light(Color.GREEN)
#     else:
#         brick.light(None)

# up/down buttons to change frequency
freq = 500
while True:
    buttons = brick.buttons()
    if Button.UP in buttons:
        brick.light(Color.GREEN)
        freq += 10
    elif Button.DOWN in buttons:
        brick.light(Color.RED)
        freq -= 10
    else:
        brick.light(None)

    brick.sound.beep(freq, 100, 30)

for i in range(20):
    print('hello world')

brick.sound.beep()

# Initialize a motor at port B.
test_motor = Motor(Port.B)

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_motor.run_target(500, 90)

# Play another beep sound.
# This time with a higher pitch (1000 Hz) and longer duration (500 ms).
brick.sound.beep(1000, 500)