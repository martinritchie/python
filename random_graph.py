def random_graph(n, k):
    # A function that creates a random graph, by Martin Ritchie
    # 08/06/2016. This funciton is a revision of my first 
    # attempt in python to code the Erdos-Renyi random graph
    # algortihtm. The code now include an adjacency list and
    # edge list as ouput in addtion to the adjacency matrix. 
    # ------------------- Inputs --------------------------
    # N: number of nodes.
    # k: desired average degree.
    # ------------------- Outputs -------------------------
    # A: adjacency matrix (line 16 for sparse).
    # A_list: adjacency list.
    # edge_list: list of edges. 
    import numpy as np
    import random
    import ipdb
    # ipdb.set_trace()
    # A = lil_matrix((n, n), dtype=np.int8)
    A_list = [[] for i in range(n)] 
    edge_list = []
    p = 1 - (float(k) / (n - 1))
    A = np.random.random((n, n))
    A *= np.tri(*A.shape)
    np.fill_diagonal(A, 0)
    
    edge = A>p 
    A[edge] = 1
    no_edge = A <= p 
    A[no_edge] = 0  # All low values set to 0
    A = np.add(A, A.transpose())

    for i in range(n):
        for j in range(i-1):
            if A[i, j] > 0: 
                A_list[i] = A_list[i] + [j]
                A_list[j] = A_list[j] + [i]
                edge_list.append((i,j))
                edge_list.append((j,i))
    return (A, A_list, edge_list) 

    