def dfsOnGraph(V,adj):
    vis = [0 for _ in range(V+1)]
    root = 1
    res = []
    dfs(root,adj,vis,res)
    return res

def dfs(node,adj,vis,res):
    vis[node] = 1
    res.append(node)
    for i in adj[node]:
        if(vis[i]!=1):
            dfs(i,adj,vis,res)
               
#             1 
#           /   \
#          /     \
#         2       3
#        / \     / \
#       4   5   6   7 

print(dfsOnGraph(7,[[],[2,3],[4,5],[6,7],[],[],[],[]])) #[1, 2, 4, 5, 3, 6, 7]
