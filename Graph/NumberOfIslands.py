#Leetcode: 200 -> This is only for 4 direction
#Solution here is for connected islands in all 8 directions
from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        vis = [[0 for _ in range(m+1)] for _ in range(n+1)]
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j] != 1:
                    res += 1
                    self.bfs(grid,i,j,n,m,vis)
        return res

    def bfs(self,grid,i,j,n,m,vis):
        q = deque()
        q.append((i,j))
        vis[i][j] = 1
        while(q):
            x,y = q.popleft()
            for d in range(8):
                if d == 0 and (x!=0 and y!=0):  #direction: NW
                    if(grid[x-1][y-1] == "1" and vis[x-1][y-1] != 1):
                        vis[x-1][y-1] = 1
                        q.append((x-1,y-1))
                elif d == 1 and (x!=0):  #direction: N
                    if(grid[x-1][y] == "1" and vis[x-1][y] != 1):
                        vis[x-1][y] = 1
                        q.append((x-1,y))
                elif d == 2 and (x!=0 and y!=m-1):  #direction: NE
                    if(grid[x-1][y+1] == "1" and vis[x-1][y+1] != 1):
                        vis[x-1][y+1] = 1
                        q.append((x-1,y+1))
                elif d == 3 and (y!=m-1):  #direction: E
                    if(grid[x][y+1] == "1" and vis[x][y+1] != 1):
                        vis[x][y+1] = 1
                        q.append((x,y+1))
                elif d == 4 and (x!=n-1 and y!=m-1):  #direction: SE
                    if(grid[x+1][y+1] == "1" and vis[x+1][y+1] != 1):
                        vis[x+1][y+1] = 1
                        q.append((x+1,y+1))
                elif d == 5 and (x!=n-1):  #direction: S
                    if(grid[x+1][y] == "1" and vis[x+1][y] != 1):
                        vis[x+1][y] = 1
                        q.append((x+1,y))
                elif d == 6 and (x!=n-1 and y!=0):  #direction: SW
                    if(grid[x+1][y-1] == "1" and vis[x+1][y-1] != 1):
                        vis[x+1][y-1] = 1
                        q.append((x+1,y-1))
                elif d == 7 and (y!=0):  #direction: W
                    if(grid[x][y-1] == "1" and vis[x][y-1] != 1):
                        vis[x][y-1] = 1
                        q.append((x,y-1))




        