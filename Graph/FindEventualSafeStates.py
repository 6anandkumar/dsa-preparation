#Leetcode: 802
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        vis=[0 for _ in range(n)]
        path=[0 for _ in range(n)]
        for i in range(n):
            if(not vis[i]):
                self.dfs(i,graph,vis,path)
        for i in range(n):
            if path[i]==0:
                res.append(i)
        return res

    def dfs(self,node,graph,vis,path):
        vis[node] = 1
        path[node] = 1
        for e in graph[node]:
            if not vis[e]:
                if(self.dfs(e,graph,vis,path)):
                    return True
            elif path[e]:
                return True
        path[node]=0
        return False
    # Alternative solution using Kahn's Algo after reversing the direction of edges
    # def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    #     n = len(graph)
    #     adj = [[] for _ in range(n)]
    #     for i in range(n):
    #         for e in graph[i]:
    #             adj[e].append(i)
    #     indegree = [0 for _ in range(n)]
    #     for i in range(n):
    #         for e in adj[i]:
    #             indegree[e] += 1
    #     q = deque()
    #     for i in range(n):
    #         if indegree[i] == 0:
    #             q.append(i)
    #     topoSort = []
    #     self.bfs(q,indegree,adj,topoSort)
    #     return sorted(topoSort)
        
    # def bfs(self,q,indegree,adj,res):
    #     while(q):
    #         k = q.popleft()
    #         res.append(k)
    #         for e in adj[k]:
    #             indegree[e] -= 1
    #             if not indegree[e]:
    #                 q.append(e)