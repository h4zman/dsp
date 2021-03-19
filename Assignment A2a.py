#Reference https://stackoverflow.com/questions/22566692/python-how-to-plot-graph-sine-wave

#Reference1 Dayang, Fara and Firzada, Danial





import matplotlib.pyplot as plt



import numpy as np





Fs = 10000

f = 1

sample = 10000

c = np.arange(sample)

s = np.sin(2 * np.pi * f * c / Fs)



ss = np.sign(s)



stri= 2/np.pi*np.arcsin(s)



sint=-s

for n in range(2,3000):

    sint = sint + (-1)**n * np.sin(2*np.pi*n*f*c/Fs)/n



ssaw= - 2 / np.pi * sint







plt.figure(1)

plt.suptitle('Sine Wave, Square Wave, Triangle Wave and Sawtooth Wave')

plt.subplot(411)

plt.plot(s, '-b', color='black')

plt.ylabel('duty cycle')

plt.xlabel('sample(n)')

plt.subplot(412)

plt.plot(ss, '-g',color='green')

plt.ylabel('duty cycle')

plt.xlabel('sample(n)')

plt.subplot(413)

plt.plot(stri, '-y', color='cyan')

plt.ylabel('duty cycle')

plt.xlabel('sample(n)')

plt.subplot(414)

plt.plot(ssaw, '-r', color='magenta')

plt.ylabel('duty cycle')

plt.xlabel('sample(n)')



plt.show()

Task 4

#Reference https://matplotlib.org/users/installing.html

#Reference1 https://stackoverflow.com/questions/17297048/opening-a-wave-file-in-python-unknown-format-49-whats-going-wrong

#Reference2 https://stackoverflow.com/questions/2060628/reading-wav-files-in-python

#Reference3 https://docs.python.org/3/library/wave.html?highlight=wav#module-wave





import wave

import numpy as np

import matplotlib.pyplot as plt

 v = wave.open('/Users/abc/OneDrive/Desktop/V1.wav' , 'r')

 sig = v.readframes(-1)

 sig = np.fromstring(sig, "Int16")



 plt.figure(1)



 plt.title("V wave")

Text(0.5, 1.0, 'V wave')

 plt.plot(sig)



 plt.show()



 sw=v.getsampwidth()

 bitd= sw*8

 nc = v.getnchannels()

 sr = v.getframerate()

 br = sr *bitd *nc

 print ('Bitrate is=' ,br , 'bps')



 print ('Samplerate is =', sr , 'Hz')