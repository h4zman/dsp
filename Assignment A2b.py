#http://wellesleynlp.github.io/spring16/speechAnalysis/index.html

#https://docs.python.org/3.3/library/stdtypes.html?highlight=range

#https://stackoverflow.com/questions/37120969/how-can-we-use-scipy-signal-resample-to-downsample-the-speech-signal-from-44100

#https://stackoverflow.com/questions/52073649/read-multiple-wav-file-from-computer-and-merge-them-to-numpy-arrays

#audacity for the sample rate value to split the audio

#Question 1

The word from the recording can be distinguished by seeing the sample wave plot from the matplotlib. There is a pause (which seen as none or small frequency on the sample). The signal of interest is then cut using range function on python.

from scipy.io import wavfile as wv

from matplotlib import pyplot as plt

import numpy as np

from scipy.signal import decimate



samplerate, data = wv.read('C:\\Users\\HaHaH\\OneDrive\\Desktop\\V1.wav')



plt.figure(1)



plt.title('Original')



plt.plot(data)



hi = data[range(19000, 41000)]

my = data[range(42000, 55900)]

name = data[range(56000, 67000)]

iz = data[range(68000, 81600)]

MH = data[range(82000,137000)]





plt.figure(2)



plt.suptitle('Original, Hi, My, Name, Is, Muhammad Hazman')



plt.subplot(611)



plt.plot(data)



plt.subplot(612)



plt.plot(hi)



plt.subplot(613)



plt.plot(my)



plt.subplot(614)



plt.plot(name)



plt.subplot(615)



plt.plot(iz)



plt.subplot(616)



plt.plot(MH)



plt.show()



#Question 2



rearrange = np.concatenate((hi, iz, my, name, MH),axis=0)



plt.figure(3)



plt.suptitle('Original vs Rearranged')



plt.subplot(211)



plt.plot(data)



plt.subplot(212)



plt.plot(rearrange)



plt.show()



wv.write('C:\\Users\\HaHaH\\OneDrive\\Desktop\\Rearrange.wav', samplerate, rearrange)



#Question 3



name1 = MH * 3



amplified = np.concatenate((hi, iz, my, name, name1),axis=0)



plt.figure(4)



plt.suptitle('Rearrange Normal vs Rearrange Amplified')



plt.subplot(211)

plt.plot(rearrange)



plt.subplot(212)

plt.plot(amplified)



plt.show()



wv.write('C:\\Users\\HaHaH\\OneDrive\\Desktop\\Amplified.wav', samplerate, amplified)



#Question 4 thanks to classmates for helping on the array equation



print('Sample rate is =', samplerate)



downsample = amplified



for i in range(0,len(downsample)):

    if i%4==0:

        downsample[i]=amplified[i]

    else:

        downsample[i]=0

        

wv.write('Downsample.wav',samplerate,downsample)

    

plt.figure(5)



plt.title('Downsample')



plt.plot(downsample)



plt.show()

