# Kruskal's Algorithm is for finding Minimum Spanning Tree (MST)
# This algo uses DisjointSet Data Structure and Union, Find functions
# Steps: 
# 1. Sort all the edges by weight in ascending order
# 2. Apply Union-Find to all the edges one-by-one   (Can do either Union By Rank or Union By Size)
#

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
    
"""input edges are in the format edges[i]=[from,to,w]
but edges needed in format: (w, (from,to)) so that we can sort edges by weight
"""
def mst(V, edges):
    new_edges = []
    for f,t,w in edges:
        new_edges.append((w,(f,t)))
    new_edges.sort()
    
    ds = DisjointSet(V)
    mst_cost = 0
    for w,(f,t) in new_edges:
        #If ultimate parents of from and to nodes are not same that means they are disjoint, union needs to be called
        if(ds.find(f) != ds.find(t)):
            mst_cost += w
            ds.union_by_rank(f,t)
    return mst_cost