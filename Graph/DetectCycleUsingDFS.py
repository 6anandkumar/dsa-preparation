def detectCycles(arr):
    n = len(arr)
    vis = [0 for _ in arr]
    for i in range(n):
        if vis[i] != 1:
            if(dfs(i,i,arr,vis)):
                return True
    return False

def dfs(node,parent,arr,vis):
    vis[node] = 1
    for e in arr[node]:
        if vis[e] != 1:
            vis[e] = 1
            if(dfs(e,node,arr,vis)):
                return True
        elif e!=parent:
            return True
    return False

print(detectCycles([[],[2,3],[1,4],[1],[2],[6],[5],[8,9],[7,9],[7,8]])) #True
print(detectCycles([[],[2,3],[1,4],[1],[2],[6],[5],[8],[7,9],[8]])) #False
            