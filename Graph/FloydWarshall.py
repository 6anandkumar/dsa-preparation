# This Algorithm is for calculating multi-source shortest path
# This is a bruteforce approach which runs in O(V^3)
# This can also be achieved by Dijkstra's Algo in a loop but the TC will be - 
# normal TC for dijkstra - O(ElogV) for V loops O(VElogV) 
# in worst case(for completed graphs where every node is connected to every other node) E = V^2 
# therefor TC for Dijkstra's algo in worst case = O(V^3logV) which is worse than O(V^3)
# This takes adjacency matrix as input

import math
def shortestPath(matrix):
    V = len(matrix)
    #Assuming each self v to v cost is marked as 0 in matrix and if there is not direct edge, it is marked as inf
    # If not set those first
    
    # Setting Assumptions here (required for gfg)
    for i in range(V):
            for j in range(V):
                if matrix[i][j] == -1:
                    matrix[i][j] = math.inf
                if i==j:
                    matrix[i][j] = 0
    
    for v in range(V):
        for i in range(V):
            for j in range(V):
                matrix[i][j] = min(matrix[i][j], matrix[i][v]+matrix[v][j])
    
    #Setting -1 back for unreachable nodes (required for gfg)
    for i in range(V):
        for j in range(V):
            if matrix[i][j] == math.inf:
                matrix[i][j] = -1
    
    # Note - This Algo will work for -ve weights but If there is a negative cycle in graph, this might not work
    # To check:
    for i in range(V):
        for j in range(V):
            if i==j and matrix[i][j] < 0:   #In -ve cycle Self node will become less than 0
                return "Graph has -ve cycles"
    return matrix