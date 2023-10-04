def detectCycle(adj):
    n = len(adj)
    vis = [0 for _ in range(n)]
    path = [0 for _ in range(n)]
    for i in range(n):
        if(dfs(0,adj,vis,path)):
            return True
    return False
def dfs(node,adj,vis,path):
    vis[node] = 1
    path[node] = 1
    for e in adj[node]:
        if vis[e] != 1:
            if(dfs(e,adj,vis,path)):
                return True
        elif path[e]==1:
            return True
    path[node] = 0
    return False
    
    