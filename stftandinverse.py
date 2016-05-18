from __future__ import division
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
import cv2
import math

fs, x = scipy.io.wavfile.read('input.wav')

# to cut the long file into a appropriate size
start = 19 #unit in secs
end = 23 #unit in secs
startnum = start*fs
endnum = end*fs
x=(zip(*x[startnum:endnum]))
x=x[0]

# output the cutted session
scipy.io.wavfile.write('outori.wav',fs,np.array(x))

N = len(x)
time = np.arange(N) / fs

# spectrogram plotting
winlen=2048
hop=128 
f, t, Sxx2 = signal.spectrogram(x, fs, nperseg=winlen, noverlap=winlen-hop,return_onesided=False, mode='complex') # the options are essential for the reconstruction
plt.figure()
plt.pcolormesh(t, f[0:winlen/2], np.absolute(Sxx2[0:winlen/2]))
plt.ylabel('Frequency [Hz]')
plt.ylim(0, 4000)
plt.xlabel('Time [sec]')
plt.savefig('complex')

def istft(X, fs, T, winlen, hop):
    x = np.zeros(T*fs)
    print("empty sound length="+str(len(x)))

    print("X shape="+str(X.shape))
    for n,i in enumerate(range(0, len(x)-winlen, hop)):
    	print("n="+str(n))
    	print("i="+str(i))
    	print("i+winlen="+str(i+winlen))
    	x[i:i+winlen] += scipy.real(scipy.ifft(X.T[n]))
    x = x/max(x)
    return x

s2=istft(Sxx2, fs, N/fs, winlen, hop)

# plot the waveform
# tlist=scipy.linspace(0, N/fs, N, endpoint=False)
# plt.figure()
# plt.plot(tlist, s2)
# plt.show()

# write the reconstruction
scipy.io.wavfile.write('out.wav',fs,s2)