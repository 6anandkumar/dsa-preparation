#Extension of Kahn's Algo
from collections import deque
def detectCycle(adj):
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
    #res is topological sort of all the nodes
    #but if there is a cycle in the graph the topo sort array will not have all the nodes from the graph
    if(len(res)<n):
        return True
    return False
    
def bfs(adj,q,indegree,res):
    while(q):
        i = q.popleft()
        res.append(i)
        for e in adj[i]:
            indegree[e] -= 1
            if indegree[e] == 0:
                q.append(e)