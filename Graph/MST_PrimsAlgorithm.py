# Prim's Algorithm is for finding Minimum Spanning Tree (MST)
# Spanning Tree is a tree which has all the nodes and n-1 edges and all nodes are reachable from every other node
# Minimum Spanning Tree is the one with least sum of weights of edges
# Very Similar to Dijktra's Algo
from heapq import heappush as push, heappop as pop
def MST(adj):
    n = len(adj)
    vis = [0 for _ in range(n)]
    q = []
    push(q,(0,0,-1))
    
    mst = []
    cost = 0
    #Prim's Algo
    while(q):
        c,k,p = pop(q)
        if vis[k]:
            continue
        vis[k] = 1
        cost += c
        mst.append((k,p))
        for e,w in adj[k]:
            if(vis[e] != 1):
                push(q, (w,e,k))
    
    # total mst sum of edges = cost
    # if required to print the mst, the adj list is list(mst)
    return cost
    