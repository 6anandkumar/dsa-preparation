#Leetcode: 947
from typing import List
class DisjointSet:
    rank = []
    parent = []
    size = []
    def __init__(self, V) -> None:
        self.rank = [0 for _ in range(V+1)] #Doing V+1 so that this can be used for both 0-indexed and 1-indexed graphs
        self.parent = [v for v in range(V+1)]
        self.size = [1 for i in range(V+1)]
    
    # find() will find the ultimate parent of a node and also compress path
    def find(self,node):
        if(self.parent[node] == node):
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
            
    # this is union by size
    def union_by_size(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return True
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = 0
        m = 0
        for i,j in stones:
            n = max(n,i)
            m = max(m,j)
        # Consider each row and col as a node and connect rows and cols that have stones
        ds = DisjointSet(n + m + 1)
        nodes_with_stones = {}
        for i,j in stones:
            r = i
            c = n+j+1
            ds.union_by_size(r,c)
            nodes_with_stones[r] = 1
            nodes_with_stones[c] = 1

        connected_components = 0
        for i in nodes_with_stones:
            if ds.find(i) == i:
                connected_components += 1
        return len(stones) - connected_components
        

