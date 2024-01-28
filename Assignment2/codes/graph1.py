import matplotlib.pyplot as plt
import numpy as np
with open(r"values.dat") as file:
    data_str = file.read()
sequences = data_str.split('\n')
sequences = np.array(sequences)[np.where(np.array(sequences) != "")].tolist()
data_array = np.array(list(map(np.vectorize(float), map(lambda line: line.split('\t'), sequences))))
x = data_array[:, 0].astype(int)
y = data_array[:, 1]
plt.xlim(0,20)
plt.ylim(0, 2500)
plt.stem(x, y,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("S(n)")
plt.xticks(np.arange(0,21, 1))
plt.yticks(np.arange(0,2500, 100))
#plt.grid(True)
plt.savefig("Figure_1.png")
plt.show()
