import matplotlib.pyplot as plt
import numpy as np
with open("values.dat") as file:
    data_str = file.read()
sequences = data_str.split('\n')
sequences = [line for line in sequences if line]
data_array = np.array([list(map(float, line.split('\t'))) for line in sequences])
x = data_array[:, 0].astype(int)
y1 = data_array[:, 1]
y2 = data_array[:, 2]
plt.xlim(0,50)
plt.ylim(0, 50)
plt.stem(x, y1,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(0,50, 5))
plt.yticks(np.arange(0,50, 5))
plt.grid(True)
plt.savefig("Figure_1.png")
plt.show()
plt.clf()
plt.xlim(0,50)
plt.ylim(-25,25)
plt.stem(x, y2,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(0,50, 5))
plt.yticks(np.arange(-25,26, 5))
plt.grid(True)
plt.savefig("Figure_2.png")
plt.show()
