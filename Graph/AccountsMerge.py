#Leetcode: 721
from typing import List
class DisjointSet:
    parent = []
    rank = []
    def __init__(self,V):
        self.parent = [i for i in range(V+1)]
        self.rank = [0 for _ in range(V+1)]
    
    def find(self,u):
        if(self.parent[u] == u):
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if(parent_u == parent_v):
            return
        if(self.rank[parent_u] < self.rank[parent_v]):
            self.parent[parent_u] = parent_v
        elif(self.rank[parent_v] < self.rank[parent_u]):
            self.parent[parent_v] = parent_u
        else:
            self.parent[parent_u] = parent_v
            self.rank[parent_v] += 1
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        e_dict = {}
        for i in range(n):
            for j in accounts[i][1:]:
                if j not in e_dict:
                    e_dict[j] = i
                else:
                    ds.union(e_dict[j],i)
        
        res = [[] for _ in range(n)]
        for i in e_dict:
            res[ds.find(e_dict[i])].append(i)
        ans = []
        for i in range(n):
            if len(res[i]):
                ans.append([accounts[i][0]] + sorted(res[i]))
        return ans
