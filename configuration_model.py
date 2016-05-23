def configuration_model(D):
   "The deleted configuration model"
   # Created by Martin Ritchie.
   # 19/05/2016.
   # Input:
   # D; a degree sequence.
   # Output: 
   # A; adjacency matrix in sparse format. 
   import numpy as np
   import random
   from scipy.sparse import lil_matrix
   # bin will store nodes from which pairs are selected to form edges. 
   # int8 will not be suitable for high degrees. 
   bin = np.zeros(sum(D),dtype=np.int8)
   k = 0
   for i in range(len(D)):
      for j in range(D[i]):
         # filling bin from D
         bin[k] = i
         k = k + 1

   np.random.shuffle(bin)
   N = len(D)
   A = lil_matrix((N, N), dtype=np.int8)
   while bin.size:
      A[bin[-1],bin[-2]] = A[bin[-1],bin[-2]] + 1
      A[bin[-2],bin[-1]] = A[bin[-2],bin[-1]] + 1
      # Not sure if this is the most efficient, or elegant, way of removing elements from the end of an array?
      bin = np.delete(bin,-1)
      bin = np.delete(bin,-1)

  
   return A 