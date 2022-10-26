# plotdata.py  Analyzing data with numpy

import numpy as np
from matplotlib import pyplot as plt

# load data
trials = np.loadtxt(fname='data.txt', comments='#', skiprows=0, delimiter=',')

# find stimulus levels
stimlevels = np.unique(trials[:,1])

# find performance at each stimulus level
pcorrect = np.zeros(stimlevels.shape)
for i, s in enumerate(stimlevels):
    f = trials[:,1]==s
    pcorrect[i] = trials[f,2].mean()

# plot proportion correct against stimulus level
plt.plot(stimlevels,pcorrect,'ro')
