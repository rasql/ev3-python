#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.parameters import SoundFile

emotions = ['SHOUTING', 'CHEERING', 'CRYING']
numbers = 'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE'.split()

for sound in emotions:
    file = eval('SoundFile.'+sound)
    brick.sound.file(file, 100)

for sound in numbers:
    file = eval('SoundFile.'+sound)
    brick.sound.file(file, 100)


