import matplotlib.pyplot as plt
import numpy as np
with open("values.dat") as file:
    data_str = file.read()
sequences = data_str.split('\n')
sequences = np.array(sequences)[np.where(np.array(sequences) != "")].tolist()
data_array = np.array(list(map(np.vectorize(float), map(lambda line: line.split('\t'), sequences))))
x = data_array[:, 0].astype(int)
y1 = data_array[: , 1]
y2 = data_array[:, 2]
plt.xlim(0, 20)
plt.ylim(0, 2500)
plt.stem(x, y2, markerfmt='o', linefmt='b-', basefmt='b-') 
plt.scatter(x, y2, color='blue')  
plt.xlabel("n")
plt.ylabel("y(n)")
plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(0, 2500, 100))

index_y6 = np.where(x == 6)[0][0]
plt.stem(x[index_y6], y2[index_y6], markerfmt='o', linefmt='r-', basefmt='r-')

#plt.grid(True)
plt.savefig("Figure_1.png")
plt.show()
plt.clf()
plt.xlim(0,20)
plt.ylim(0, 750)
plt.stem(x, y1,markerfmt='o')
#plt.title("Plotting x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xticks(np.arange(0,21, 1))
plt.yticks(np.arange(0,750, 50))
#plt.grid(True)
plt.savefig("Figure_2.png")
plt.show()
