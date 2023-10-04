#Leetcode:1091
from typing import List
from heapq import heapify,heappush as push, heappop as pop
import math
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if(grid[0][0]==1):
            return -1
        n = len(grid)
        q = []
        heapify(q)
        dist = [[math.inf for _ in range(n)] for _ in range(n)]
        vis = [[0 for _ in range(n)] for _ in range(n)]
        push(q,[1,0,0])
        dist[0][0] = 1
        vis[0][0] = 1
        self.bfs(grid,dist,q,n,vis)
        return dist[-1][-1] if dist[-1][-1]!=math.inf else -1
    def bfs(self,grid,dist,q,n,vis):
        dr = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        while(q):
            d,x,y = pop(q)
            for e in range(8):
                if (0<=x+dr[e][0]<=n-1 and 0<=y+dr[e][1]<=n-1) and grid[x+dr[e][0]][y+dr[e][1]] == 0 and d+1 < dist[x+dr[e][0]][y+dr[e][1]] and vis[x+dr[e][0]][y+dr[e][1]]!=1:
                    dist[x+dr[e][0]][y+dr[e][1]] = d+1
                    vis[x+dr[e][0]][y+dr[e][1]] = 1
                    push(q,[d+1,x+dr[e][0],y+dr[e][1]])
