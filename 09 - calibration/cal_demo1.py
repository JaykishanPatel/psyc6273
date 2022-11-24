import numpy as np
import matplotlib.pyplot as plt
import calibrate as cal

g = cal.GammaFit()

g.grey = np.linspace(start=0, stop=255, num=20).round()
g.lum = 90 * ( (g.grey/255)**2.2 ) + 10 + np.random.normal(size=g.grey.size)

g.plot()
plt.show()

g.fit()
g.plot()
plt.show()

g.save('cal.pickle')
