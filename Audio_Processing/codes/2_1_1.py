import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.loadtxt("2_1_1.dat", delimiter=',')

# Extract x values and indices
indices = data[:, 0]
x_values = data[:, 1]

# Plot the graph without the base line
plt.stem(indices, x_values)
plt.xlabel('Index')
plt.ylabel('x[n]')
plt.title('Plot of x[n]')
plt.grid(True)
plt.savefig("2_1_1.png")
#plt.show()
