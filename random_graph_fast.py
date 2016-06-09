def random_graph_fast(n, k):
    # A function that creates a random graph, by Martin Ritchie
    # 08/06/2016. This funciton is a revision of my first 
    # attempt in python to code the Erdos-Renyi random graph
    # algortithm. This particular code does not require any loops
    # to create a graph. It is signifciantly faster than my other
    # implementation but will not return the adjacency or edge list 
    # ------------------- Inputs --------------------------
    # N: number of nodes.
    # k: desired average degree.
    # ------------------- Outputs -------------------------
    # A: adjacency matrix.
    import numpy as np
    import random
    p = 1 - (float(k) / (n - 1))
    A = np.random.random((n, n))
    # The upper triangle part set to zeros.
    A *= np.tri(*A.shape)
    # Set the diagonal to zeros. 
    np.fill_diagonal(A, 0)
    # Now round the values to {0,1} depending on p.
    edge = A>p 
    A[edge] = 1
    no_edge = A <= p 
    A[no_edge] = 0 
    A = np.add(A, A.transpose())
    return (A) 

    