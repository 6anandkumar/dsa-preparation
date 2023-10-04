#Shortest Distance in and undirected graph from a source with unit weights
from collections import deque
import math
def shortestDistance(adj,source):
    n = len(adj)
    vis = [0 for _ in range(n)]
    q = deque()
    q.append((source,0))
    dist = [math.inf for _ in range(n)]
    bfs(q,adj,vis,dist)
    return dist

def bfs(q,adj,vis,dist):
    while(q):
        k,d = q.popleft()
        dist[k] = d
        vis[k] = 1
        for e in adj[k]:
            if not vis[e]:
                vis[e] = 1
                q.append((e,d+1))

print(shortestDistance([[1,3],[0,2,3],[1,6],[0,4],[3,5],[4,6],[2,5,7,8],[6,8],[6,7]],0))