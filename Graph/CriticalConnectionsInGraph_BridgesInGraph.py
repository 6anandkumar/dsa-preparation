# Leetcode: 1192
# This is solved using Tarjan's Algorithm
from typing import List
class Solution:
    timer = 1
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for i,j in connections:
            adj[j].append(i)
            adj[i].append(j)
        vis = [0 for _ in range(n)]
        tin = [0 for _ in range(n)] #Time of insertion
        low = [0 for _ in range(n)] #Lowest time of insertion
        bridges = []
        for i in range(n):
            if not vis[i]:
                self.dfs(i,-1,vis,adj,tin,low,bridges)
        return bridges
    def dfs(self,i,parent,vis,adj,tin,low,bridges):
        vis[i] = 1
        tin[i] = self.timer
        low[i] = self.timer
        self.timer += 1
        for e in adj[i]:
            if e == parent: continue
            if not vis[e]:
                self.dfs(e,i,vis,adj,tin,low,bridges)
                low[i] = min(low[i],low[e])
                if low[e] > tin[i]: #This means there is no way for e to reach i, hence this is a bridge
                    bridges.append([i,e])
            else:
                low[i] = min(low[e],low[i])



