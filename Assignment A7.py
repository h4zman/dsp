#Ref https://tomroelandts.com/articles/how-to-create-a-simple-low-pass-filter
#Ref https://americodias.com/docs/python/audio_python.md
#Ref https://tomroelandts.com/articles/spectral-reversal-to-create-a-high-pass-filter
#Ref https://dsp.stackexchange.com/questions/41098/implementing-a-band-pass-filter-from-scratch

import math
import numpy as np
import scipy.fftpack as fft
from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy import signal

samplerate, signal1 = wavfile.read('D:/Download/message.wav')

#find sample rate and sample number
print("Sample Rate is",samplerate)
print("Sample Number is", len(signal1))

#analyze noise using spectogram and find frequency cutoff
plt.figure(1)
plt.specgram(signal1,Fs=samplerate)
plt.ylabel("Sample / 2")
plt.xlabel("Time (s)")

#based on understanding it should be fL = fc/samplerate/2 to get 0 < fc < 0.5 but dont know why when I do that it amplifies the noise instead.
#or can use noise1 = 3769/len(signal1)/2, noise2= 25130/len(signal1)/2 if we use fft.fft(signal1)

fc = 310/samplerate  
fc1 = 1999/samplerate 
N = 21 #order
n = np.arange(N) #create an array size for N

#create window, hamming window.
window= 0.54 - 0.46 * np.cos(2*np.pi*(np.arange(N)) / (N-1)) 
 
#Lowpass Noise 1
lp = np.sinc(2 * fc * (n - (N-1) / 2)) #sinc wave lp

#multiply by window
lp =lp * window
lp = lp/np.sum(lp)
plt.figure(2)
plt.plot(lp) 
plt.title("LP Noise 1 filter")
plt.ylabel("Amplitude")
plt.xlabel("Point")

# Lowpass Noise 2
lp2 = np.sinc(2 * fc1 * (n - (N-1) / 2))
lp2 =lp2* window
lp2 = lp2/np.sum(lp2)
plt.figure(3)
plt.plot(lp2) 
plt.title("LP Noise 2 filter")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

#Inverse LP > HP
lp2 = lp2 * (-1) ** np.arange(N)
plt.figure(4)
plt.plot(lp2)
plt.title("LP > HP Noise Filter")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

# Combine LP + HP = Bandreject
h = lp + lp2
plt.figure(5)
plt.plot(h) 
plt.title("BP Filter")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

#add padding to filter to give same samplerate size, fft to see the window frequcney
padband = np.concatenate((h,np.zeros(8000-N)))
fftpad = fft.fft(padband)
log= 20*np.log10(fftpad)
plt.figure(6)
plt.subplot(211)
plt.plot(fftpad)
plt.title("Windowed Sinc Linear")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.subplot(212)
plt.plot(log)
plt.title("Windowed Sinc Log")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

impulse = fft.irfft(padband)

plt.figure(8)
plt.title('Impulse Response')

plt.plot(impulse)


#convol filter + original signal to filter signal
newsignal= np.convolve(padband,signal1)
plt.figure(7)
plt.specgram(newsignal,Fs=len(padband))
plt.title("Spectogram to see noise")
plt.ylabel("Sample / 2")
plt.xlabel("Time (s)")
wavfile.write('C:\\Users\\HaHaH\\OneDrive\\Desktop\\filter.wav',samplerate,newsignal.astype(signal1.dtype))

plt.show()