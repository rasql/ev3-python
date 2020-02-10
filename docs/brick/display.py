#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.parameters import ImageFile
from pybricks.tools import print, wait

images = 'RIGHT FORWARD ACCEPT QUESTION_MARK STOP_1 LEFT DECLINE \
    THUMBS_DOWN BACKWARD NO_GO WARNING STOP_2 THUMBS_UP'.split()

for image in images:
    brick.display.clear()
    brick.display.text(image, (10, 10))
    file = eval('ImageFile.'+image)
    brick.display.image(file, clear=False)
    wait(1000)