#Leetcode: 1319
# Solved using union find in a disjoint set
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if(len(connections)<n-1):
            return -1
        connections.sort()
        ds = DisjointSet(n)
        mst = 0
        for f,t in connections:
            if(ds.find(f) != ds.find(t)):
                mst += 1
                ds.union(f,t)
        c = 0
        for i in range(n):
            if(ds.find(i) == i):
                c += 1
        return c-1