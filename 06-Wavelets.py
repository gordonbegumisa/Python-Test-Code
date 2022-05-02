import pywt
import numpy as np
from scipy.signal import chirp, sweep_poly
import matplotlib.pylab as plt

import numpy as np
from scipy.fft import fftshift
from matplotlib import mlab


t = np.linspace(0, 1, 5001)
# w = chirp(t, f0=12.5, f1=2.5, t1=10, method='hyperbolic')
# plot.plot(t, w)
w = np.sin(15*np.pi/(0.8-t)) + np.sin(5*np.pi/(0.8-t))
plt.plot(t, w, c='red')
plt.show()



