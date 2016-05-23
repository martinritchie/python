def random_graph(N, k):
   "This function creates a random graph"
   # Created by Martin Ritchie.
   # 19/05/2016.
   # Input:
   # N; number of nodes, 
   # k; desired average degree. 
   # Output: 
   # A; adjacency matrix in sparse format. 
   import numpy as np
   import random
   from scipy.sparse import lil_matrix
   A = lil_matrix((N, N), dtype=np.int8)
   p = float(k)/(N-1)
   # Create a lower triangular matrix.
   for i in range(N):
   		for j in range(i):
   			if random.random() < p:
   				A[i,j] = A[i,j] + 1 
   # Copy the lower to upper triangular part.
   A = A + A.transpose()
   return A 