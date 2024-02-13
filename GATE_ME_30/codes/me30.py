import matplotlib.pyplot as plt
import numpy as np
with open("values.dat") as file:
    data_str = file.read()
sequences = data_str.split('\n')
sequences = np.array(sequences)[np.where(np.array(sequences) != "")].tolist()
data_array = np.array(list(map(np.vectorize(float), map(lambda line: line.split('\t'), sequences))))
t = data_array[:, 0]  # the time axis values
x = data_array[: , 1] # values of x(t)

plt.plot(t,x)  
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.savefig("Figure_1.png")
#plt.show()
