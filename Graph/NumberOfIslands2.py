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

def numberOfIslands(n,m,queries):
    vis = [[0 for _ in range(m)] for _ in range(n)]
    ds = DisjointSet(m*n)
    res = []
    isles = 0
    drc = [(-1,0),(0,1),(1,0),(0,-1)]
    for i,j in queries:
        if(vis[i][j]==1):
            res.append(isles)
            continue
        isles += 1
        for d in range(4):
            x=i+drc[d][0]
            y=j+drc[d][1]
            if 0<=x<=n-1 and 0<=y<=m-1 and vis[x][y]!=0:
                u = (m*i) + j
                v = (m*x) + y
                if(ds.find(u) != ds.find(v)):
                    ds.union_by_rank(u,v)
                    isles -= 1
        vis[i][j]=1
        res.append(isles)
    return res

print(numberOfIslands(4,5,[(0,0),(0,0),(1,1),(1,0),(0,1),(0,3),(1,3),(0,4),(3,2),(2,2),(1,2),(0,2)]))
                
    