import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

SPS = 300 				# Hz
dt = 1/SPS 				# sec

# Frequency (Hz) of the signals

f1 = 5 	
f2 = 50
f3 = 100

T = 10					# Time (s) duration of the signals
N = int(T*SPS)				# Length of the sample
df = 1/T

X = np.linspace(0, T, N)

Y = 5*np.sin(2*np.pi*f1*X) + 3*np.sin(2*np.pi*f2*X) + 8*np.sin(2*np.pi*f3*X)
Y = Y + 15*np.random.randn(N)		# Add the random noise

Fy = 2*fft.fft(Y)			# 2 because we are ignoring the power in the -ve frequency  

# Lets compute frequency array

freq = np.arange(0, N//2)*df		# We ignore the N/2 to N and consider only +v Frequency  Coefficients 

plt.figure(figsize=[12,9])
plt.plot(freq, np.abs(Fy[:N//2]), color='g')
plt.xlabel('Frequency [Hz]' )
plt.ylabel('Fourier Transform')
plt.title('Foruier Domain')
plt.axvline(x=5, color='r', ls='--', lw=0.5)
plt.text(6, 5000, 'f = 5 Hz', color='r')
plt.axvline(x=50, color='r', ls='--', lw=0.5)
plt.text(51, 5000, 'f = 50 Hz', color='r')
plt.axvline(x=100, color='r', ls='--', lw=0.5)
plt.text(101, 5000, 'f = 100 Hz', color= 'r')
plt.grid(alpha=0.3, color='c')
plt.show()
