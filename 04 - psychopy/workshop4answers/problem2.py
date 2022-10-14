# problem2.py  Solution to workshop 4, problem 2

from psychopy import visual, event

# open window
win = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)

# create grating object
wavelength = 20.0   # grating wavelength (pixels)
delta = 0.1         # increment in phase each frame
grating = visual.GratingStim(win=win, mask='gauss', size=500, pos=[0,0], sf=1/wavelength)

# initialize motion state
moving = True

# loop indefinitely
while True:

    # update phase
    if moving:
        grating.phase += delta

    # show grating
    grating.draw()
    win.flip()

    # check for keypress
    keys = event.getKeys()
    if keys:
        if 'q' in keys:
            break
        else:
            moving = not moving

# close window
win.close()
