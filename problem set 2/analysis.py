# analysis.py  Analyze circle centering data

import numpy as np

# load data
data = np.loadtxt('data.txt', delimiter=',')

# find mean distance over all trials
x = data[:,3]
y = data[:,4]
d = np.sqrt( x**2 + y**2 )
dmean = d.mean()

print(f'mean distance: {dmean:.2f}\n')
