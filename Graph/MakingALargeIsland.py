#Leetcode: 827
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
    
    # union() will attach both v1 and v2 if disjoint - this is union by rank
    def union_by_rank(self,V1,V2):
        ultimate_parent_v1 = self.find(V1)
        ultimate_parent_v2 = self.find(V2)
        if(ultimate_parent_v1 == ultimate_parent_v2):
            return
        if(self.rank[ultimate_parent_v1] < self.rank[ultimate_parent_v2]):
            self.parent[ultimate_parent_v1] = ultimate_parent_v2
        elif(self.rank[ultimate_parent_v1] > self.rank[ultimate_parent_v2]):
            self.parent[ultimate_parent_v2] = ultimate_parent_v1
        else:
            self.parent[ultimate_parent_v1] = ultimate_parent_v2
            self.rank[ultimate_parent_v2] += 1
            
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
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        drc = [(-1,0),(0,1),(1,0),(0,-1)]
        res = 0
        ds = DisjointSet(n*n)
        for i in range(n):
            for j in range(n):
                if(grid[i][j] != 1):
                    continue
                for d in range(4):
                    x = i + drc[d][0]
                    y = j + drc[d][1]
                    if 0<=x<=n-1 and 0<=y<=n-1 and grid[x][y]==1:
                        u = n*i + j
                        v = n*x + y
                        # if ds.find(u) != ds.find(v):
                        ds.union_by_size(u,v)
        res = max(res,max(ds.size))
        for i in range(n):
            for j in range(n):
                if(grid[i][j] != 0):
                    continue
                parents = []
                for d in range(4):
                    x = i + drc[d][0]
                    y = j + drc[d][1]
                    if 0<=x<=n-1 and 0<=y<=n-1 and grid[x][y]==1:
                        v = n*x + y
                        parents.append(ds.find(v))
                
                current_sizes = 1
                for p in set(parents):
                    current_sizes += ds.size[p]
                res = max(res,current_sizes)


        return res
