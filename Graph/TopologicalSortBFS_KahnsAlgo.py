from collections import deque
def topoSort(adj):
    n = len(adj)
    indegree = [0 for _ in range(n)]
    for i in range(n):
        for e in adj[i]:
            indegree[e] +=1
    q = deque()
    for i in range(n):
        if not indegree[i]:
            q.append(i)
    res = []
    bfs(adj,q,indegree,res)
    return res
    
def bfs(adj,q,indegree,res):
    while(q):
        i = q.popleft()
        res.append(i)
        for e in adj[i]:
            indegree[e] -= 1
            if indegree[e] == 0:
                q.append(e)

print(topoSort([[],[],[3],[1],[0,1],[0,2]]))