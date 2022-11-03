# workshop6answers.py  Solutions to lecture 6 workshop problems

# Solve the following problems using the numpy module.

# 1. Create a 2D array of zeros, of size (10,20).

import numpy as np

x = np.zeros(shape=(10,20))

# 2. Create a 2D array of size (5,10), where every entry is 100.
#    hint: Read the help for np.tile(). Recall that you can get this help
#    text at the command line by running "help( np.tile )", after
#    importing the numpy module as np. Alternatively there's lot of help
#    available online for almost any numpy function.

x = np.tile(100, reps=(10,20))

# 3. Create a 2D array of random integers between 1 and 10, of size (5,5).
#    hint: read the help for np.random.randint()

x = np.random.randint(low=1, high=11, size=(10,20))

# 4. Repeat problem 3, but this time specify that the values in the array
#    should be of type np.int8.

x = np.random.randint(low=1, high=11, size=(10,20), dtype=np.int8)

# 5. Repeat problem 3, but this time make the array size (m,n),
#    where m and n are themselves random integers between 1 and 10. That is,
#    every time you create the array, it has a randomly generated size.

m = np.random.randint(low=1, high=11)
n = np.random.randint(low=1, high=11)
# or, in a single line:
m, n = np.random.randint(low=1, high=11, size=(2,))

x = np.random.randint(low=1, high=11, size=(m,n))

# 6. (a) Create a 2D array x of normally distributed random numbers, with
#        mean zero and standard deviation one. Make the array size (9,9).
#        hint: Use the function np.random.normal().
#    (b) Create a 2D array y that is a view of the central 3 x 3 square
#        of the array x that you created in part (a).
#        hint: Use the slice operations we covered in the lecture,
#        e.g., something like y = x[0:1,0:1]
#    (c) Set the values of y to zero (in place), and confirm that this also
#        changes the values of the central 3 x 3 square of x to zero.

x = np.random.normal(size=(9,9))
y = x[3:6,3:6]
y[:] = 0
print(x)

# 7. (a) Write a function that creates an array that is an image of a circle,
#        where the pixels outside the circle have a value of zero, and the
#        pixels inside the circle have a value of one. Give the function
#        an argument 'size' that controls the size of the image in pixels, and
#        an argument 'radius' that controls the radius of the circle in pixels.
#        hint: Model your answer after the gabor() function that we created
#        in the lecture code.
#    (b) Use matplotlib's plot function to show an image of a circle created
#        using the function you wrote for part (a).

def circle(radius=30, size=(128,128)):
    xmat =   np.fromfunction(lambda i, j: j, shape=size) - np.floor(size[1]/2)
    ymat = -(np.fromfunction(lambda i, j: i, shape=size) - np.floor(size[0]/2))
    dmat = np.sqrt(xmat**2 + ymat**2)
    return np.float64(dmat<radius)

from matplotlib import pyplot as plt

im = circle(radius=20, size=(64,64))
plt.imshow(im, cmap='gray')
plt.show()
