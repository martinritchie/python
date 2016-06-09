# This script is used to simulate epidemics on networks. The script
# takes the average for each S, I, and R count, saves the data in 
# CSR files. 
execfile('random_graph.py')
execfile('gillespie_lists.py')
import numpy as np
import matplotlib.pyplot as plt
#A = np.ones((100,100)) - np.identity(100)
numsims = 10
dpoints = 250
S = np.zeros(dpoints,dtype=np.float32)
I = np.zeros(dpoints,dtype=np.float32)
R = np.zeros(dpoints,dtype=np.float32)

for x in range(numsims): 
	A, A_list, edge_list = random_graph(1000,5)
	s, i, r, T = gillespie_lists(A_list, 10, 2, 1, 10, dpoints)
	S = S + s
	I = I + i
	R = R + R
	print(x)
S = (S) / numsims
I = (I) / numsims
R = (R) / numsims


np.savetxt("S.csv", S, delimiter=",")
np.savetxt("I.csv", I, delimiter=",")
np.savetxt("T.csv", T, delimiter=",")

plt.plot(T,I)
plt.show()
