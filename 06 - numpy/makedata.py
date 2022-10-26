# makedata.py  Make a file of simulated behavioural data

import numpy as np
import scipy.stats

# set parameters
ntrials = 200
stimlevels = np.linspace(-1.0, 1.0, 10)
sigma = 0.5

# make simulated data
trialnum = np.arange(ntrials)
stim = np.random.choice(stimlevels, size=ntrials)
pcorrect = scipy.stats.norm.cdf(stim, loc=0.0, scale=sigma)
correct = np.random.binomial(1,pcorrect)
rt = 0.100 + (np.random.normal(size=ntrials) ** 2)

# write simulated data to a text file
data = np.column_stack((trialnum,stim,correct,rt))
np.savetxt('data.txt',data,fmt=('%3d,%7.4f,%d,%6.4f'))
