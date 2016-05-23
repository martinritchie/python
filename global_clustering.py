def global_clustering(A):
   "This function computes the global clustering  coefficient"
   # Created by Martin Ritchie.
   # 21/05/2016.
   # Input: 
   # A; adjacency matrix in sparse format. 
   # Output: 
   # C; the global clustering coefficient
   import numpy as np
   A2 = A*A; 
   A3 = A2*A;
   Triangles = int(A3.trace())
   Triples = A2.sum() - int(A2.trace())
   C = float(Triangles) / Triples
   return C 