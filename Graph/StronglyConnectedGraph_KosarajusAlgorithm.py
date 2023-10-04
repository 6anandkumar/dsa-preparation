# Strongly Connected Components - group of nodes where each node is reachable from every other node in the group
# Is only possible in directed graphs
# Solved Using Kosaraju's Algorithm
# Steps:
# 1. Sort all the edges according to finishing time - can be done using normal DFS
# 2. Reverse the graph
# 3. Do a DFS on the reversed graph according to the order of finishing time

def NumberOfSCG(adj):   #Kosaraju's Algo
    V = len(adj)
    
    #Step 1:
    vis = [0 for _ in range(V)]
    stack = []
        #TC: O(V+E) time taken by DFS
    for i in range(V):
        if not vis[i]:
            dfs(i,vis,adj,stack)
    #Step 2:
    adj_reversed = [[] for _ in range(V)]   #SC: O(V+E)
        #TC: O(V+E)
    for i in range(V):
        for e in adj[i]:
            adj_reversed[e].append(i)
    #Step 3:
    scc_count = 0
    vis = [0 for _ in range(V)]
        #TC: O(V+E)
    while(stack):
        node = stack.pop()
        if not vis[node]:
            scc_count += 1
            dfs(node,vis,adj_reversed,[])
    
    return scc_count

def dfs(i,vis,adj,stack):
    vis[i] = 1
    for e in adj[i]:
        if not vis[e]:
            dfs(e,vis,adj,stack)
    stack.append(i)