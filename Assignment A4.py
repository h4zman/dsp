import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as ft

#before this i am using 10000 fs and sample. Due to f value = 1, i have to change the sample to 100
#or else the graph will not really give a readable plot
Fs = 100
f = 1
sample = 100
c = np.arange(sample)
s = np.sin(2 * np.pi * f * c / Fs)

xa= np.arange(sample//2)
#sq
ss = np.sign(s)
ssTF = ft.fft(ss) #fft square
#tri
stri= 2/np.pi*np.arcsin(s)
striTF= ft.fft(stri) #fft triangle

sint=-s
for n in range(2,3000):
    sint = sint + (-1)**n * np.sin(2*np.pi*n*f*c/Fs)/n
#saw
ssaw= - 2 / np.pi * sint
ssawTF = ft.fft(ssaw) #fft sawtooth

plt.figure(1)
plt.title("Square Wave")
plt.ylabel('voltage(V)')
plt.xlabel('sample(n)')
plt.plot(xa,abs(ssTF[:sample//2]))

plt.figure(2)
plt.title("Triangle Wave")
plt.ylabel('voltage(V)')
plt.xlabel('sample(n)')
plt.plot(xa,abs(striTF[:sample//2]))

plt.figure(3)
plt.title("Sawtooth Wave")
plt.ylabel('voltage(V)')
plt.xlabel('sample(n)')
plt.plot(xa,abs(ssawTF[:sample//2]))
plt.show()

#Given a signal, y that is composed of a 2 unit DC, 0.5kHz Square wave, 1.5kHz Triangle wave and 2kHz Sawtooth wave:
#Plot y for a duration of 1 second and a sampling frequency of 10kHz. Label the x-axis using time unit.
#Plot Y. Label the x-axis using actual frequency unit.

#create new Square
nFs = 10000
nsample = 10000
fss = 500
i = np.arange(nsample)
ns = np.sin(2 * np.pi * fss * i / nFs)
nss = np.sign(ns)
ts = 1/nFs
t = np.arange(0, 1, ts)   
xb =np.arange(nsample//2)
#create new triangle

ftri = 1500
nstri = np.sin(2*np.pi*ftri*i/nFs)
newTri = 2/np.pi*np.arcsin(nstri)

#create new sawtooth

fsaw = 2000
nsaw = np.sin(2*np.pi*fsaw*i/nFs)
sint=-nsaw
for n in range(2,3000):
    sint = sint + (-1)**n * np.sin(2*np.pi*n*fsaw*i/nFs)/n

nssaw= - 2 / np.pi * sint

#compose
y = 2 + nss + newTri + nssaw
fftmix = ft.fft(y)
plt.figure(4)
plt.title('Time Domain of composed wave')
plt.ylabel('amplitude')
plt.xlabel('time(s)')
plt.plot(t,y)


#compose fft
plt.figure(5)
plt.title('FFT of composed mix wave')
plt.ylabel('Amplitude')
plt.xlabel('frequency (Hz)')
plt.plot(xb,abs(fftmix[:nsample//2]))

#Question 3 concatenate
z = np.zeros(10000)
y_pad = np.concatenate((y,z))
ffty_pad = ft.fft(y_pad)
plt.figure(6)
plt.title('Y_Pad Plot')
plt.xlabel('Freq (Hz)')
plt.ylabel('Amplitude')
plt.plot(xb,abs(ffty_pad[:nsample//2]))
plt.show()

#Question 4 noise
#y_noise_10pct = y + randn(1, 10000)*0.1
#y_noise_30pct = y + randn(1, 10000)*0.3
#y_noise90pct = y + randn(1, 10000)*0.9


y_noise_10pct = y + np.random.randn(10000) * 0.1
y_noise_30pct = y + np.random.randn(10000) * 0.3
y_noise90pct = y + np.random.randn(10000) * 0.9

fftY_noise10 = ft.fft(y_noise_10pct)
fftY_noise30 = ft.fft(y_noise_30pct)
fftY_noise90 = ft.fft(y_noise90pct)

plt.figure(7)
plt.title('FFT Noise 10%')
plt.xlabel('Freq (Hz)')
plt.ylabel('Amplitude')
plt.plot(xb,abs(fftY_noise10[:nsample//2]))
plt.figure(8)
plt.title('FFT Noise 30%')
plt.xlabel('Freq (Hz)')
plt.ylabel('Amplitude')
plt.plot(xb,abs(fftY_noise30[:nsample//2]))
plt.figure(9)
plt.title('FFT Noise 90%')
plt.xlabel('Freq (Hz)')
plt.ylabel('Amplitude')
plt.plot(xb,abs(fftY_noise90[:nsample//2]))

plt.show()

#ref
#https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
#https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html
#https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
#https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.randn.html
#http://learninghub.upm.edu.my/blastdk/pluginfile.php/199576/mod_resource/content/3/W4b%20-%20ECC3403%20%281%29.pdf