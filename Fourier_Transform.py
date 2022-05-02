import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from numpy.fft import fft, fftfreq, ifft
sns.set()

n = 1000 # number of points
Lx = 100 # Length in metres

omega =2.0 * np.pi/Lx # frequency/time (sec)

# create composite signal
t = np.linspace(0,Lx,n)
a = 1.0*np.cos(5.0*omega*t)
a1 = 0.5*np.sin(10.0*omega*t)
a2= 2.0*np.sin(20.0*omega*t)
a = a+a1+a2

z = 0+1j
f=0.212
g = a*np.exp(t*f*z)

freq = fftfreq(n) # creates all frequencies
mask = freq > 0 # ignore 1/2 of all values
fft_val = fft(a)
fft_theo = 2.0*np.abs(fft_val/n) # true theoretical value

plt.figure(1)
plt.title('Original Signal g(t)')
plt.plot(t, a, color='red', label="Original")


plt.figure(3)
plt.title('Function g(mega)')

plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.plot(g.real, g.imag, color='blue', label="Original")

plt.figure(2)
plt.title('true FFT Values g-bar(omega)')
plt.plot(freq[mask], fft_theo[mask], label='FFT Values')

plt.show()


