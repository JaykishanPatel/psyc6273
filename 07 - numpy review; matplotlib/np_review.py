# np_review.py  Review of basics of the numpy module

import numpy as np

# a few ways of creating arrays

x = np.zeros(shape=(3,4))
x = np.ones(shape=(3,4))
x = np.empty(shape=(3,4))
x = np.full(shape=(3,4), fill_value=10)

x = np.random.normal(loc=0.0, scale=1.0, size=(3,4))
x = np.random.uniform(low=0.0, high=1.0, size=(3,4))

# - transform a sequence into a 1D array
x = np.array([ 1.0, 2.0, 3.0 ])  # transform a list
x = np.array(( 1.0, 2.0, 3.0 ))  # transform a tuple

# - transform a sequence of sequences into a 2D array
x = np.array([ [ 1.0, 2.0, 3.0 ], [ 4.0, 5.0, 6.0 ] ])  # list of lists
x = np.array([ ( 1.0, 2.0, 3.0 ), ( 4.0, 5.0, 6.0 ) ])  # list of tuples

# - create 1D sequences of numbers
x = np.arange(10)
x = np.linspace(start=0.0, stop=100.0, num=6)

# - load data from a text file
x = np.loadtxt(fname='data.txt', comments='#', skiprows=0, delimiter=',')

# some important attributes of an array
x.ndim      # number of dimensions
x.shape     # size of each dimension
x.size      # total number of elements
x.dtype     # data type of elements

# arithmetic operations apply to whole arrays

x = np.random.normal(size=(3,4))
y = np.random.normal(size=(3,4))

z = x + y
z = x - y
z = x * y
z = x / y

# functions that apply to whole arrays

u = np.exp(x)
v = np.log(u)
# others: all, any, argmax, argmin, ceil, clip, corrcoef, cov, cross, cumprod,
# cumsum, diff,  dot, floor, inner, max, mean, median, min, prod, round, sort,
# std, sum, trace, transpose, var

# indexing and slicing

x = np.random.normal(size=(10,5))

y = x[2,3]      # pick a single element: row, column; result is a number, not an array
y = x[0:5,1]    # multiple rows; result is a 1D array
y = x[:,1]      # all rows; result is a 1D array
y = x[1:3,:]    # multiple rows, all columns; result is a 2D array

x[:,1] = 0      # can also assign new values to parts of an array
