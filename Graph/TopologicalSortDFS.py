def topSort(adj):
    n = len(adj)
    vis=[0 for _ in range(n)]
    stack = []
    for i in range(n):
        if not vis[i]:
            dfs(i,adj,vis,stack)
    res = []
    while(stack):
        res.append(stack.pop())
    return res

def dfs(node,adj,vis,stack):
    vis[node] = 1
    for e in adj[node]:
        if vis[e] != 1:
            dfs(e,adj,vis,stack)
    stack.append(node)

print(topSort([[],[],[3],[1],[0,1],[0,2]]))