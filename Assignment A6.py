import numpy as np
import scipy.fftpack as fft
from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy import signal

samplerate,signal1 = wavfile.read('C:\\Users\\HaHaH\\OneDrive\\Desktop\\message.wav')

print("sample rate", samplerate)

#plot original signal in time domain
plt.figure(1)
plt.plot(range(0,len(signal1)),signal1)
plt.title("original signal in td")
plt.ylabel('Amp')
plt.xlabel('Time(s)')



#fft using rfft to get real value array.
d = fft.rfft(signal1)



#sample length for freq domain 'd'
sample =len(d)
print(sample)
#plot spectrum analysis in freq domain to find the noise
plt.figure(2)
plt.title("Spectrum Analysis")
plt.xlabel('Freq')
plt.ylabel('Amp')
plt.plot(d) 

#split audio according to the rfft plot noise
part1= d[range(0,7199)]
part2= d[range(7200,7700)] #noise
part3= d[range(7701,47999)]
part4= d[range(48000,51999)] #noise
part5= d[range(52000,100000)]

#build ideal filter. i dont use conditional is because if i place 
#only 0 at noise range and 1 at others, the filter become inverted 
#and i dont know why, so i do manually to sort the signal.
temp = np.zeros(sample)
for i in range(1, sample):

    if (i in range( 0, 7199)):
        temp[i]= 1
#noise range 1
    elif (i in range(7200,7700)):
        temp[i] = 0
    
    elif (i in range(7701, 47999)):
        temp[i] = 1
#noise range 2
    elif ( i in range(48000, 51999)):
        temp[i] = 0

    elif ( i in range(52000,100000)):
        temp[i] = 1
    
    else:
        temp[i] = 1
  
#multiply to cancel out noise on original signal
filter1 = np.zeros(sample)
for i in range(1, sample):
    filter1[i] = d[i] * temp[i]


#inverse rfft the signal back
ifft_back = fft.irfft(filter1)

#amplify signal to get louder volume
amplify = ifft_back * 10

plt.figure('test')
plt.title('Ideal Filter Created for Freq Domain')
plt.xlabel('Freq')
plt.ylabel('Amp')
plt.plot(temp)

plt.figure('filter sample')
plt.title('Signal in Freq Domain after filter noise')
plt.xlabel('Sample')
plt.ylabel('Amp')
plt.plot(filter1)

plt.figure('td')
plt.title('Signal after irfft and amplified')
plt.xlabel(' Sample')
plt.ylabel('Amp')
plt.plot(amplify)

system = d, amplify

#impulse response
impulse = fft.irfft(temp)

plt.figure('impulse')
plt.title('Impulse Response')

plt.plot(impulse)


wavfile.write('C:\\Users\\HaHaH\\OneDrive\\Desktop\\filter.wav',samplerate,amplify.astype(signal1.dtype))






plt.show()