from collections import deque
def BFS(nodes, adj):
    q = deque()
    visited = [0 for _ in range(nodes+1)]
    bfs = []
    root = 1
    q.append(root)
    visited[root] = 1
    while(q):
        i = q.popleft()
        bfs.append(i)
        for j in adj[i]:
            if visited[j] != 1:
                visited[j] = 1
                q.append(j)
    return bfs

#             1
#           /   \
#         /       \
#        2         3
#     /    \     /   \
#    4      5   6     7

print(BFS(7,[[],[2,3],[4,5],[6,7],[],[],[],[]]))    #[1, 2, 3, 4, 5, 6, 7]
            
    