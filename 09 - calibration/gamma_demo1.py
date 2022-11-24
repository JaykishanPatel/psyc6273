import time
import numpy as np
from psychopy import visual, event

# open window and mouse
win = visual.Window(size=[800, 600], units='pix', waitBlanking=True, fullscr=False)
mouse = event.Mouse(win=win)

# record the current gamma lookup table
oldlut = visual.gamma.getGammaRamp(0)

# create and assign a new lookup table that shows only red colours
ramp = np.arange(1024)/1023
zero = np.zeros(1024)
lut = np.row_stack((ramp,zero,zero))
visual.gamma.setGammaRamp(0,lut)

# now we'll just do some arbitrary PsychoPy thing that we've done before.
# I've chosen to run the mouse-cursor-tracking program we saw a few lectures
# ago. note, though, how the colours we use for the stimuli are modified by
# the lookup table. here, all colours become red, regardless of what RGB
# values we specify for the circle that tracks the mouse cursor.

# create a circle for tracking the mouse
stim = visual.Circle(win, fillColor=(-0.5,-0.5,-0.5), lineColor=None, radius=25)

# loop indefinitely
while True:

    # get mouse position
    x, y = mouse.getPos()
    x += win.size[0]/4
    y += win.size[1]/4

    # draw the circle
    stim.setPos((x,y))
    stim.draw()
    win.flip()

    # quit on mouse button press
    if mouse.getPressed()[0]:
        break

# restore the gamma table
visual.gamma.setGammaRamp(0,oldlut)

# close window
win.close()
