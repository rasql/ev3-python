#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait

images = 'RIGHT FORWARD ACCEPT QUESTION_MARK STOP_1 LEFT DECLINE \
    THUMBS_DOWN BACKWARD NO_GO WARNING STOP_2 THUMBS_UP'.split()

for image in images:
    brick.display.text(image.lower())
    wait(1000)
