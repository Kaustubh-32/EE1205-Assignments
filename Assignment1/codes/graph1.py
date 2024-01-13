import matplotlib.pyplot as plt
import numpy as np
a = np.arange(-25, 26)
y = np.array([7 + (a1-1)*6 if a1 > 1 else 0 for a1 in a])
plt.xlim(-25,25)
plt.ylim(0, 50)
plt.stem(a, y,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(-25, 26, 5))
plt.yticks(np.arange(0, 50, 5))
plt.grid(True)
plt.show()
