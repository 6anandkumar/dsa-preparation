# Shortest Distance from a source to any edge in a Directed Acyclic Graph(DAG)
# Adjacency List will contain edges and their weights 
# ex - [[(1,2),(2,2)],[],[]] where node 0 is connected to node 1(with weight 2) and also to node 2(with weight 2)
import math
def shortestDistance(adj,source):
    n = len(adj)
    
    #Step 1 - Find Topological Ordering of nodes
    stack = []
    vis = [0 for _ in range(n)]
    for i in range(n):
        if vis[i]!=1:
            dfs(i,adj,vis,stack)
    print(stack)
    #Step 2 - Take the nodes out of stack and relax edges(idk what does this mean :) )
    dist = [math.inf for _ in range(n)]
    dist[source] = 0
    while(stack and stack[-1] != source):
        stack.pop()

    while(stack):
        k = stack.pop()
        for e,w in adj[k]:
            dist[e] = min(dist[e], dist[k]+w)
                
    return dist

def dfs(node,adj,vis,stack):
    vis[node] = 1
    for e,w in adj[node]:
        if vis[e]!=1:
            dfs(e,adj,vis,stack)
    stack.append(node)
# 
#  0 -(2)-> 1
#  |        |
# (1)      (3)
#  |        | 
#  4 -(2)-> 2
#  |        |
# (4)      (6)
#  |        | 
#  5 -(1)-> 3
#
print(shortestDistance([[(1,2),(4,1)],[(2,3)],[(3,6)],[],[(5,4),(2,2)],[(3,1)]],0))