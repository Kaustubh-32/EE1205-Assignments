import matplotlib.pyplot as plt
import numpy as np
a = np.arange(-25, 26)
y = np.array([18 - (a1-1)*(2.5) if a1 > 1 else 0 for a1 in a])
plt.xlim(-25,25)
plt.ylim(-25,25)
plt.stem(a, y,markerfmt='o')
plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(-25, 26, 5))
plt.yticks(np.arange(-25,26, 5))
plt.grid(True)
plt.show()