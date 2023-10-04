from collections import deque
def detectCycles(arr):
    n = len(arr)
    q = deque()
    vis = [0 for _ in range(n)]
    for i in range(n):
        if vis[i] != 1:
            q.append((i,i))
            if(bfs(arr,vis,q)):
                return True
    return False
            
def bfs(arr,vis,q):
    while(q):
        k,p = q.popleft()
        vis[k] = 1
        for j in arr[k]:
            if(vis[j] != 1):
                vis[j] = 1
                q.append((j,k))
            else:
                if j != p:
                    return True
    return False
                

print(detectCycles([[],[2,3],[1,4],[1],[2],[6],[5],[8,9],[7,9],[7,8]])) #True
print(detectCycles([[],[2,3],[1,4],[1],[2],[6],[5],[8],[7,9],[8]])) #False