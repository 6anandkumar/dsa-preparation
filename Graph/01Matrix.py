#Leetcode: 542
from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        res = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if(mat[i][j] == 0):
                    q.append([i,j,0])
        self.bfs(vis,q,mat,n,m,res)
        return res

    def bfs(self,vis,q,mat,n,m,res):
        while(q):
            i,j,k = q.popleft()
            res[i][j]=k
            for d in range(4):
                if d==0 and (i!=0): #Direction: N
                    if(mat[i-1][j] != 0 and vis[i-1][j]!=1):
                        vis[i-1][j] = 1
                        q.append([i-1,j,k+1])
                elif d==1 and (j!=m-1): #Direction: E
                    if(mat[i][j+1] != 0 and vis[i][j+1]!=1):
                        vis[i][j+1] = 1
                        q.append([i,j+1,k+1])
                elif d==2 and (i!=n-1): #Direction: S
                    if(mat[i+1][j] != 0 and vis[i+1][j]!=1):
                        vis[i+1][j] = 1
                        q.append([i+1,j,k+1])
                elif d==3 and (j!=0): #Direction: W
                    if(mat[i][j-1] != 0 and vis[i][j-1]!=1):
                        vis[i][j-1] = 1
                        q.append([i,j-1,k+1])

