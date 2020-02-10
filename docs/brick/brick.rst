EV3 Brick
=========

This section shows how to program the buttons, lights, sounds and display.

Buttons
-------

This program associates 3 button presses with 3 different colors:

* LEFT - green
* CENTER - yellow
* RIGHT - red

.. literalinclude:: button.py

Sound
-----

This program uses the 4 buttons to change volume and frequency.

* LEFT/RIGHT - change volume from 0 to 100 in increments of 10
* UP/DOWN - change frequency in increments of 10

.. literalinclude:: sound.py

This program places a couple of sound files into two lists:

* emotions
* numbers

Inside a loop they are played in sequence.

.. literalinclude:: sound2.py

Display
-------

This program displays image files and their name on the screen, during 1 second.

.. literalinclude:: display.py

This program writes a new line of text to screen, every second.

.. literalinclude:: display2.py


Battery
-------

This program displays the battery voltage and current during 5 seconds.

.. literalinclude:: battery.py





