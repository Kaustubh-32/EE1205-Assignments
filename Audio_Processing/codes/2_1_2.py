import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.loadtxt("2_1_2.dat", delimiter=',')

# Extract x values and indices
indices = data[:, 0]
y_values = data[:, 1]

# Plot the graph without the base line
plt.stem(indices, y_values)
plt.xlabel('Index')
plt.ylabel('y[n]')
plt.title('Plot of y[n]')
plt.grid(True)
plt.savefig("2_1_2.png")
#plt.show()
