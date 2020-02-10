#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait

voltage = brick.battery.voltage()
current = brick.battery.current()

brick.display.text('voltage = {} mV'.format(voltage))
brick.display.text('current= {} mA'.format(current))

wait(5000)
