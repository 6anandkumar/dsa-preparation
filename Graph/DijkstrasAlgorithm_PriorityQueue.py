# Dijkstra's Algo : Shortest path algo from source to any node
# Using Priority Queue (Min Heap)   TC - O(E*logV)  E-Number of Edges, V-Number of Nodes
# This can be implemented both using priority queue and normal queue
from heapq import heapify,heappop as pop, heappush as push
from collections import deque
import math
def shortestPath(adj,source):
    n = len(adj)
    q = []
    heapify(q)
    # q = deque()
    dist = [math.inf for _ in range(n)]
    push(q,(0,source))
    # q.append((0,source))
    dist[0]=0
    bfs(adj,q,dist)
    return dist

def bfs(adj,q,dist):
    while(q):
        d,k = pop(q)
        # d,k = q.popleft()
        for e,w in adj[k]:
            if d+w  < dist[e]:
                dist[e] = d+w
                push(q, (d+w,e))
                # q.append((d+w,e))

print(shortestPath([[(1,4),(2,4)],[(0,4),(2,2)],[(0,4),(1,2),(3,3),(4,1),(5,6)],[(2,3),(5,2)],[(2,1),(5,3)],[(2,6),(3,2),(4,3)]],0))