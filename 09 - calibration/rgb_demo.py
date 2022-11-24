
from psychopy import visual, core

win = visual.Window(size=[800, 600], units='pix', colorSpace='rgb255', color=(128, 128, 128), waitBlanking=True, fullscr=False)

circle = visual.Circle(win, colorSpace='rgb255', fillColor=(200, 200, 200), lineColor=None, radius=25)
circle.draw()
win.flip()

core.wait(1)

win.close()
