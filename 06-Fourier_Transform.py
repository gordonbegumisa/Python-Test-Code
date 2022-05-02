import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from scipy.fftpack import fft
sns.set()

limit = 5
i = 0.001
t = np.arange(1, limit, i)

# create composite signal a(t)
f = 1
a = 3*np.sin(2*np.pi*f*t)
f += 3
a += np.sin(2*np.pi*f*t)
f += 3
a += 0.5 * np.sin(2*np.pi*f*t)

# Analysing Function dot product g(t)
i = 1j
f = 1
g1 = a*np.exp(-i*2*np.pi*f*t)
f += 3
g2 = a*np.exp(-i*2*np.pi*f*t)
f += 3
g3 = a*np.exp(-i*2*np.pi*f*t)

# Draw with analysing function
f = 1

# FFT
sr = 2000
X = fft(a)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T

plt.figure(2)
plt.title('Function g(f)')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.plot(g1.real, g1.imag, color='blue', label="Original Signal")
plt.plot(g2.real, g2.imag, color='red', label="Original Signal")
plt.plot(g3.real, g3.imag, color='green', label="Original Signal")

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")

plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 20)

plt.subplot(122)
plt.plot(t, a, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
