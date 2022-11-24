import numpy as np
import matplotlib.pyplot as plt
import calibrate as cal

g = cal.GammaFit('cal.pickle')

g.plot()
plt.show()

lum = np.array([20,30,40])
print(lum)

grey = g.lum2grey(lum)
print(grey)

cal.setgamma()
