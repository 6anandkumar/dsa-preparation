# Print Shortest Path from source to any node 
# Solved using Dijkstra's Algo
from heapq import heapify,heappush as push, heappop as pop
import math
def shortestPath(adj,source,dest):  #graph is weighted
    n = len(adj)
    q = []
    heapify(q)
    parent = [i for i in range(n)]
    dist = [math.inf for _ in range(n)]
    dist[source] = 1
    push(q,(0,source))
    
    #BFS:
    while(q):
        d,k = pop(q)
        for e,w in adj[k]:
            if d+w < dist[e]:
                dist[e] = d+w
                push(q, (d+w,e))
                parent[e] = k
    if(dist[dest] == math.inf):
        return []
    else:
        path = []
        node = dest
        while(parent[node] != node):
            path.append(node)
            node = parent[node]
        path.append(node)
    return list(reversed(path))
    
print(shortestPath([[(1,4),(2,4)],[(0,4),(2,2)],[(0,4),(1,2),(3,3),(4,1),(5,6)],[(2,3),(5,2)],[(2,1),(5,3)],[(2,6),(3,2),(4,3)]],0,5))  #[0,2,4,5]