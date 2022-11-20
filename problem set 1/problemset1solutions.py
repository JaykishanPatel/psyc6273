# problemset1solutions.py

# 1(a)

import random

ntrials = 100

stimnum = [ random.choice([1,2,3]) for i in range(ntrials) ]
rt = [ 0.1 + random.gauss(0,1)**2 for i in range(ntrials) ]
correct = [ random.uniform(0,1)<0.80 for i in range(ntrials) ]

# 1(b)

rt1 = [ rt[i] for i in range(ntrials) if stimnum[i]==1 ]
mean1 = sum(rt1)/len(rt1)

# 1(c)

rt2 = [ rt[i] for i in range(ntrials) if stimnum[i]==2 and correct[i] ]
mean2 = sum(rt2)/len(rt2)

# 1(d)

def rtsamp(fast):
    if fast:
        return 0.1 + random.gauss(0,1)**2
    else:
        return 0.3 + random.gauss(0,1)**2

# or more concisely:
rtsamp = lambda fast : random.gauss(0,1)**2 + ( 0.1 if fast else 0.3 )

rt3 = [ rtsamp(not correct[i]) for i in range(ntrials) ]

# 2

def normclip(n=1):
    x = []
    for i in range(n):
        while True:
            y = random.gauss(0,1)
            if y>=-2 and y<=2:
                break
        x.append(y)
    return x
