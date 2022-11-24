import numpy as np
from psychopy import visual
from psychopy.hardware import keyboard

# open window and keyboard
# win = visual.Window(size=[800, 600], units='pix', waitBlanking=True, fullscr=False)
win = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)
kb = keyboard.Keyboard()

# make an image of vertical strips, with rgb increasing from (0,0,0) to (255,255,255)
dim = np.array(win.size/2,dtype=np.int64)
jvec = -1 + 2*np.arange(dim[0])/(dim[0]-1)
im = np.tile(jvec,(dim[1],1))

# show the image
stim = visual.ImageStim(win, image=im, size=im.T.shape)
stim.draw()
win.flip()

# initialize which row of the lookup table will be nonzero
k = 0

# loop indefinitely
while True:

    # adjust nonzero row of lookup table according to keypress (or quit)
    keys = kb.waitKeys()
    if 'left' in keys:
        k = max(k-1,0)
    elif 'right' in keys:
        k = min(k+1,255)
    elif 'q' in keys:
        break

    # make and assign the new lookup table    
    v = np.zeros(256)
    v[k] = 1
    v = np.repeat(v,4)
    lut = np.vstack((v,v,v))
    visual.gamma.setGammaRamp(0,lut)

win.close()
