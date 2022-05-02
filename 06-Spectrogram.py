import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Create Chirp Signal
limit = 0.79999
t = np.linspace(0, limit, 5001)
w = np.sin(15*np.pi/(0.8-t)) + np.sin(5*np.pi/(0.8-t))

# Plot Signal
plt.plot(t, w)
plt.ylabel('Amplitude')
plt.xlabel('Time [sec]')
plt.title('Signal')
plt.show()

# Generate the spectrogram
fs = 1
f, t, Sxx = signal.spectrogram(w, fs)

# 2d Plot
plt.figure(figsize=(8, 10))
plt.pcolormesh(t, f, 10.0*np.log10(Sxx), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.title('Spectogram')
clb = plt.colorbar()
clb.ax.set_title('FFT Amplitude')
plt.show()

# 3d plot
fig = plt.figure()
ax = fig.gca(projection='3d')
sc = ax.plot_surface(f[:, None], t[None, :], 10.0*np.log10(Sxx), cmap = plt.cm.cividis)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Frequency [Hz]')
ax.set_zlabel('FFT Amplitude')
clb = plt.colorbar(sc)
clb.ax.set_title('FFT Amplitude')
plt.show()



