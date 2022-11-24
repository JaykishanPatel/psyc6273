import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from psychopy import visual

class GammaFit:
    
    def __init__(self, fname=''):
        super(GammaFit, self).__init__()
        self.grey = []    # greylevels (rgb) from calibration
        self.lum = []     # luminances from calibration
        self.param = {}   # fitted gamma function parameters
        if fname:
            self.load(fname)
    
    def fit(self):
        fitfn = lambda x, p: self.gammafn(x,*p)
        errfn = lambda p: np.sum( (self.lum - fitfn(self.grey,p))**2 )
        pinit = [self.lum.max()-self.lum.min(), 0, 2, self.lum.min() ]
        res = optimize.minimize(errfn, x0=pinit, method='Nelder-Mead')
        self.param = { 'k' : res.x[0], 'g0' : res.x[1], 'gamma' : res.x[2], 'delta' : res.x[3] }
    
    def plot(self):
        if self.param:
            xx = np.arange(256)
            plt.plot(xx, self.grey2lum(xx), 'r-', label='fit')
        plt.plot(self.grey, self.lum, 'bo', label='measurements')
        plt.xlabel('greylevel')
        plt.ylabel('luminance')
        plt.legend(loc='upper left')
    
    def lum2grey(self, lum, roundit=True):
        g = self.gammainv(lum,**self.param)
        return g.round() if roundit else g
    
    def grey2lum(self, grey):
        return self.gammafn(grey,**self.param)
    
    def gammafn(self, x, k, g0, gamma, delta):
    
        low = x<g0
        high = x>255
        ok = ~(low|high)
    
        y = np.empty(x.shape)
        y[low] = delta
        y[high] = k+delta
        y[ok] = k * np.power((x[ok]-g0)/(255-g0), gamma) + delta
        return y
    
    def gammainv(self, y, k, g0, gamma, delta):
    
        low = y<delta
        high = y>k+delta
        ok = ~(low|high)
    
        x = np.empty(y.shape)
        x[low] = g0
        x[high] = 255
        x[ok] = (255-g0) * np.power((y[ok]-delta)/k, 1/gamma) + g0
        return x
    
    def save(self, fname='cal.pickle'):
        with open(fname, 'wb') as f:
            pickle.dump(self.grey, f)
            pickle.dump(self.lum, f)
            pickle.dump(self.param, f)
    
    def load(self, fname='cal.pickle'):
        with open(fname, 'rb') as f:
            self.grey = pickle.load(f)
            self.lum = pickle.load(f)
            self.param = pickle.load(f)
    
    def __repr__(self):
        if self.param:
            rep = 'gamma parameters:\n'
            for k in self.param:
                rep += f'    {k:5s} = {self.param[k]:6.2f}\n'
        else:
            rep = 'no fit available\n'
        return rep

def setgamma(screenID=0, lut=[]):
    
    if not lut:
        # make a null lookup table
        lut = np.arange(256)/255
        lut = np.tile(lut,reps=(3,1))
        lut = np.repeat(lut, repeats=4, axis=1)
    
    # set lookup table
    visual.gamma.setGammaRamp(screenID, lut)
