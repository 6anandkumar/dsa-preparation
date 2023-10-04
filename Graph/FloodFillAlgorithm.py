#Leetcode: 733
from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        vis = [[0 for _ in range(m+1)] for _ in range(n+1)]
        self.bfs(image,sr,sc,color,vis,n,m)
        return image
    def bfs(self,image,sr,sc,color,vis,n,m):
        q = deque()
        q.append((sr,sc))
        ic = image[sr][sc]  #initial color
        while(q):
            x,y = q.popleft()
            vis[x][y] = 1
            image[x][y] = color
            for d in range(4):
                if d==0 and (x!=0): #direction: N
                    if(image[x-1][y]==ic and vis[x-1][y]!=1):
                        vis[x-1][y] = 1
                        image[x-1][y] = color
                        q.append((x-1,y))
                elif d==1 and (y!=m-1): #direction: E
                    if(image[x][y+1]==ic and vis[x][y+1]!=1):
                        vis[x][y+1] = 1
                        image[x][y+1] = color
                        q.append((x,y+1))
                elif d==2 and (x!=n-1): #direction: S
                    if(image[x+1][y]==ic and vis[x+1][y]!=1):
                        vis[x+1][y] = 1
                        image[x+1][y] = color
                        q.append((x+1,y))
                elif d==3 and (y!=0): #direction: W
                    if(image[x][y-1]==ic and vis[x][y-1]!=1):
                        vis[x][y-1] = 1
                        image[x][y-1] = color
                        q.append((x,y-1))
