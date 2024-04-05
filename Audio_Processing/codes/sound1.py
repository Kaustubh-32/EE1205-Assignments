import soundfile as sf
from scipy import signal
input_signal,fs = sf.read("Kk3.wav")
sample_freq = fs
order = 4
cutoff_freq = 5000.0
Wn= 2*cutoff_freq/sample_freq
b,a = signal.butter(order,Wn,'low')
print(a)
print(b)
output_signal = signal.filtfilt(b,a,input_signal)
sf.write('Sound_with_reduced_noise.wav',output_signal,fs)
