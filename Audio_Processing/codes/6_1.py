import soundfile as sf
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def custom_filtfilt(b, a, x):
    # Ensure a[0] is 1 to avoid scaling
    if a[0] != 1:
        a = a / a[0]
        b = b / a[0]

    # Pad the input signal to handle boundary effects
    pad_len = max(len(a), len(b)) - 1
    x_padded = np.pad(x, (pad_len, pad_len), mode='edge')

    # Perform forward filtering
    y_forward = signal.lfilter(b, a, x_padded)

    # Perform backward filtering
    y_backward = signal.lfilter(b, a, y_forward[::-1])[::-1]

    # Trim the result to match the length of the input signal
    y_trimmed = y_backward[pad_len:len(x_padded) - pad_len]

    return y_trimmed

# Read .wav file
input_signal, fs = sf.read('Kk3.wav') 

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4   

# Cutoff frequency 4kHz
cutoff_freq = 4000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with butterworth filter using both functions
output_signal_builtin = signal.filtfilt(b, a, input_signal)
output_signal_custom = custom_filtfilt(b, a, input_signal)

# Plotting
x_plt = np.arange(len(input_signal))

# Plotting the output of built-in function
plt.figure(figsize=(10, 6))
plt.plot(x_plt[1000:10000], output_signal_builtin[1000:10000], 'b.')
plt.title("Output by Built-in Function")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('output_builtin.png')

# Plotting the output of custom function
plt.figure(figsize=(10, 6))
plt.plot(x_plt[1000:10000], output_signal_custom[1000:10000], 'r.')
plt.title("Output by Custom Function")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('output_custom.png')
