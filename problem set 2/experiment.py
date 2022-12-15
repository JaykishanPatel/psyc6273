# experiment.py  Circle centering experiment

import math, random
from psychopy import visual, event, core
from psychopy.hardware import keyboard

# set stimulus properties
ntrials = 10               # number of trials
radius_large = 200         # radius of large, fixed circle
radius_small = 40          # radius of smaller, moveable circle
filename = 'data.txt'      # data file name

# open window
win = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)

# create keyboard and mouse objects
kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False, newPos=[0,0])

# create circles
circle_large = visual.Circle(win=win, radius=radius_large, fillColor=(0,0,0), lineColor=(1,1,1), lineWidth=2, edges=100)
circle_small = visual.Circle(win=win, radius=radius_small, fillColor=(0,0,0), lineColor=(1,1,1), lineWidth=2, edges=100)

# create clock for reaction times
clock = core.Clock()

# open data file
datafile = open(filename, 'a')

# run trials
for t in range(ntrials):

    # prepare for trial
    clock.reset()
    mouse.setPos([ random.randint(-2*radius_large, 2*radius_large) for i in range(2) ])
    
    # run trial
    while True:
        
        xy = mouse.getPos()
        xy = ( xy[0]+win.size[0]/4, xy[1]+win.size[1]/4 )
        circle_small.setPos(xy)
        
        circle_large.draw()
        circle_small.draw()
        win.flip()
        
        key = kb.getKeys(['space'])
        if key:
            datafile.write(f'{t+1}, {radius_large}, {radius_small}, {xy[0]}, {xy[1]}, {clock.getTime():.3f}\n')
            break

# shut down
datafile.close()
win.close()
