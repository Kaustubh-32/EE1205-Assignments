import numpy as np
import matplotlib.pyplot as plt

# Define x[n] and h[n]
x_n = np.arange(1, 17)
h_n = np.ones(16)

# Calculate y[n] (linear convolution)
y_n = np.convolve(x_n, h_n, mode='full')

# Calculate z[n] (IDFT of the product of DFTs of x[n] and h[n])
X_k = np.fft.fft(x_n)
H_k = np.fft.fft(h_n)
z_n = np.fft.ifft(X_k * H_k)

# Plot y[n] and z[n]
plt.figure(figsize=(10, 6))
plt.stem(range(len(y_n)), y_n, linefmt='C0-', markerfmt='C0o', basefmt='C0-', label='y[n]')
plt.stem(range(len(z_n)), z_n, linefmt='C1-', markerfmt='C1o', basefmt='C1-', label='z[n]')
plt.xlabel('n')
plt.ylabel('Value')
plt.legend()

# Highlight the equality for n = 15
plt.scatter(15, y_n[15], color='blue', marker='x', s=100, label=f'y[15] = {y_n[15]:.2f}')
plt.scatter(15, z_n[15], color='red', marker='^', s=100, label=f'z[15] = {z_n[15]:.2f}')

plt.grid(True)
plt.legend()
plt.show()
