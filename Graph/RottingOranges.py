#Leetcode: 994
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        q = deque()
        vis = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==2):
                    vis[i][j]=1
                    q.append([i,j,0])
        res = self.bfs(grid,vis,q,res,n,m)
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1 and vis[i][j]==0):
                    return -1
        return res
    def bfs(self,grid,vis,q,res,n,m):
        while(q):
            x,y,k = q.popleft()
            for d in range(4):
                if d==0 and x!=0:   #direction: N
                    if(grid[x-1][y]==1 and vis[x-1][y]!=1):
                        vis[x-1][y]=1
                        q.append([x-1,y,k+1])
                        res = max(res,k+1)
                if d==1 and y!=m-1:   #direction: E
                    if(grid[x][y+1]==1 and vis[x][y+1]!=1):
                        vis[x][y+1]=1
                        q.append([x,y+1,k+1])
                        res = max(res,k+1)
                if d==2 and x!=n-1:   #direction: S
                    if(grid[x+1][y]==1 and vis[x+1][y]!=1):
                        vis[x+1][y]=1
                        q.append([x+1,y,k+1])
                        res = max(res,k+1)
                if d==3 and y!=0:   #direction: W
                    if(grid[x][y-1]==1 and vis[x][y-1]!=1):
                        vis[x][y-1]=1
                        q.append([x,y-1,k+1])
                        res = max(res,k+1)
        return res
