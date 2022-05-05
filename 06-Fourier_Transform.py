import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from scipy.fftpack import fft
sns.set()

#  Site Time intervals
limit = 5
i = 0.001
t = np.arange(1, limit, i)

# create composite signal a(t)
f = 1
a = 1
while f < 12:
    a += (f ^ 2)*np.sin(2*np.pi*f*t)
    f += 4

# Analysing Function dot product g(t)
i = 0 + 1j
f = 1
while f < 12:
    g = a*np.exp(-i*2*np.pi*f*t)
    col = (np.random.random(), np.random.random(), np.random.random())
    plt.plot(g.real, g.imag, color=col, label="Original Signal")
    f += 5

plt.title('Function g(f)')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()

# FFT
sr = 2000
X = fft(a)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 20)

plt.subplot(122)
plt.plot(t, a, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
