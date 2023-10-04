# This is similar to critical edges in graph(bridges) but here we have to find ciritical nodes
from typing import List
class Solution:
    timer = 1
    def articulationPoints(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for i,j in connections:
            adj[j].append(i)
            adj[i].append(j)
        vis = [0 for _ in range(n)]
        tin = [0 for _ in range(n)] #Time of insertion
        low = [0 for _ in range(n)] #Lowest time of insertion
        articulation_points = []
        for i in range(n):
            if not vis[i]:
                self.dfs(i,-1,vis,adj,tin,low,articulation_points)
        return articulation_points
    def dfs(self,i,parent,vis,adj,tin,low,articulation_points):
        vis[i] = 1
        tin[i] = self.timer
        low[i] = self.timer
        self.timer += 1
        children = 0
        for e in adj[i]:
            if e == parent: continue
            if not vis[e]:
                self.dfs(e,i,vis,adj,tin,low,articulation_points)
                low[i] = min(low[i],low[e])
                if low[e] >= tin[i] and parent!=-1: #This means e is connected only through i and i is not a starting node
                    articulation_points.append(i)
                children += 1
            else:
                low[i] = min(low[e],tin[i])
        if children > 1 and parent==-1:
            articulation_points.append(i)


