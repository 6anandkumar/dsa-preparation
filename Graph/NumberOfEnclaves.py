#Leetcode: 1020
from typing import List
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j] == 1:
                        q.append([i,j])
        self.bfs(vis,q,grid,n,m)
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] != 1:
                    res+=1
        return res
    
    def bfs(self,vis,q,grid,n,m):
        while(q):
            i,j = q.popleft()
            vis[i][j] = 1
            for d in range(4):
                if d==0 and (i!=0): #Direction: N
                    if(grid[i-1][j] == 1 and vis[i-1][j]!=1):
                        vis[i-1][j] = 1
                        q.append([i-1,j])
                elif d==1 and (j!=m-1): #Direction: E
                    if(grid[i][j+1] == 1 and vis[i][j+1]!=1):
                        vis[i][j+1] = 1
                        q.append([i,j+1])
                elif d==2 and (i!=n-1): #Direction: S
                    if(grid[i+1][j] == 1 and vis[i+1][j]!=1):
                        vis[i+1][j] = 1
                        q.append([i+1,j])
                elif d==3 and (j!=0): #Direction: W
                    if(grid[i][j-1] == 1 and vis[i][j-1]!=1):
                        vis[i][j-1] = 1
                        q.append([i,j-1])