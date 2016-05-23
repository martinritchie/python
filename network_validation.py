   # This script checks that generated networks contain no significant abnormalities.
   # The intended use for this script is the analysis of smaller prototype networks.
   # Dependancies: global_clustering.py
   # Created by Martin Ritchie.
   # 21/05/2016.
import numpy as np
import scipy.sparse as sps

# Ensure that the matrix is dense. 
if sps.issparse(A):
	A = A.todense()

# Check symmetry.
if np.array_equal(A,A.transpose()):
	message = "A is undirected."
  	print message
 
# Check for multi-edges.
multi = A.max()
if multi > 1:
	num_edges =  np.sum(1*(A>1))
	message = "There are %d multi-edges." % num_edges
	print message
  
# Check self edges.
selff = int(A.trace())
if selff > 0:
  	message = "There are %d self edges." % selff

# Extract the degree sequnce.
D_post = sum(A) 
k = np.mean(D_post)
vark = np.var(k)
message = "Average degree = %d.\nVariance = %d." % (k, vark)
print message

if 'D' in locals() and np.array_equal(D,D_post):
	diff =  np.sum(D) - np.sum(D_post)
  	message = "The generated sequence has %d fewer edges than D." % diff
  	print message
  	dif_nodes = sum(1*(D==D_post))
  	message = "There are %d nodes that have the incorrect degree." % dif_nodes
  	print message

execfile('global_clustering.py')
C = global_clustering(A)
message = "C = %d." % C 
print message