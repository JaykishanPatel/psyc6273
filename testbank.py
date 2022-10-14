# testbank.py  Test bank

# 1. Create a list x that contains the numbers 1 to 10.
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


# 2. Set a variable y equal to the following sublists of x. Where possible,
# write your code so that it works for any length of x, e.g., it still
# works if x has 20 elements rather than 10.

# 2a. the first element of x
y = x[0]

# 2b. the first five elements of x
y = x[:5]

# 2c. the last element of x
y = x[-1]

# 2d. the last five elements of x
y = x[-5:]

# 2e. every third element of x, starting with the second element
y = x[1::3]

# 2f. all the elements of x, in reverse order
y = x[::-1]

# 2g. every second element of x, counting back from the last element
y = x[::-2]

# 2h. the first three elements of x and the last three elements of x
y = x[:3] + x[-3:]

# 2i. the largest element of x, repeated five times
y = 5 * [ max(x) ]

# 2j. the smallest element of x, repeated a number of times equal to
#     the largest element of x
y = max(x) * [ min(x) ]


# 3. Change the list x as follows.

# 3a. set the first element to zero
x[0] = 0

# 3b. set the last three elements to zero
x[-3:] = 3 * [0]

# 3c. delete the fourth and fifth elements of x
del x[3:5]

# 3d. delete the first occurrence of the largest element of x
x.remove(max(x))

# 3e. delete the last element of x
x.pop()

# 3f. append the value 11 to the end of x
x.append(11)

# 3g. append the first three elements of x to the end of x
x.extend(x[0:3])

# 3h. sort the elements of x
x.sort()


# 4. Make y equal to the list x, in such a way that if you change an 
#    element of x, the corresponding element of y changes as well.
y = x


# 5. Make y equal to the list x, in such a way that if you change an
#    element of x, the corresponding element of y does not change.
y = x.copy()


# 6. Create a tuple z that contains the following elements.

# 6a. the number 50
z = (50,)

# 6b. the numbers 1, 2, and 3, in that order, repeated five times
z = 5 * ( 1, 2, 3 )


# 7. Use a for loop to print the integers from 1 to 20.

for x in range(1,21):
    print(x)


# 8. Use a while loop to get a sample from the standard normal
# distribution, between -2 and 2.

import random
while True:
    x = random.gauss(0,1)
    if x>=-2 and x<=2:
        break


# 9. Use a list comprehension to make a list of the squares of the integers
# from 1 to 20.

x = [ i**2 for i in range(1,21) ]


# 10. (a) Create a dictionary with three keys that are strings, and three values
# that are integers.

diameters = { 'earth' : 12472, 'moon' : 3475, 'sun' : 1392000 }

# (b) Look up one of the values in the dictionary you just created, and assign
# it to the variable x.

x = diameters['earth']


# 11. Set x to 3.141592654. Use an f-string to print a message that reports the value
# of x with four decimal places.

x = 3.141592654
print(f'The value of x is {x:.4f}.')


# 12. Define a function f that takes two arguments, x and y, and returns
# sin(x)*cos(y). Give y a default value of zero.

import math
def f(x, y=0):
    return math.sin(x) * math.cos(y)



# 13. Write code that creates a text file containing the square of numbers 1 to 10.

f = open('squares.txt', 'w')

for i in range(1,11):
    f.write(f'{i**2}\n')

f.close()


# 14. Define a function randt(n, u, v) that returns an n-tuple of random
# floating point numbers between u and v. Give u a default value of 0,
# and v a default value of 1.

import random

def randt(n, u=0, v=1):
    x = [ random.uniform(u,v) for i in range(n) ]
    return tuple(x)


# 15. Write code that uses PsychoPy to open a window that covers
# the whole screen.

from psychopy import visual
win = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)


# 16. Write code that uses PsychoPy to show a black circle centered in
# a window called win.

stim = visual.Circle(win=win, fillColor='black', lineColor=None, radius=25)
stim.draw()
win.flip()


# 17. Write code that uses PsychoPy to get the current mouse position.

from psychopy import event
mouse = event.Mouse()
x, y = mouse.getPos()


# 18. Write code that uses PsychoPy to find which keyboard keys are
# currently being pressed.

from psychopy import event
keys = event.getKeys()


# 19. Write code that closes a PsychoPy window called win.
win.close()

