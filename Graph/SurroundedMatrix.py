#Leetcode: 130
from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if board[i][j] == "O":
                        q.append([i,j])
        self.bfs(vis,q,board,n,m)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and vis[i][j] != 1:
                    board[i][j] = "X"
    
    def bfs(self,vis,q,board,n,m):
        while(q):
            i,j = q.popleft()
            vis[i][j] = 1
            for d in range(4):
                if d==0 and (i!=0): #Direction: N
                    if(board[i-1][j] == "O" and vis[i-1][j]!=1):
                        vis[i-1][j] = 1
                        q.append([i-1,j])
                elif d==1 and (j!=m-1): #Direction: E
                    if(board[i][j+1] == "O" and vis[i][j+1]!=1):
                        vis[i][j+1] = 1
                        q.append([i,j+1])
                elif d==2 and (i!=n-1): #Direction: S
                    if(board[i+1][j] == "O" and vis[i+1][j]!=1):
                        vis[i+1][j] = 1
                        q.append([i+1,j])
                elif d==3 and (j!=0): #Direction: W
                    if(board[i][j-1] == "O" and vis[i][j-1]!=1):
                        vis[i][j-1] = 1
                        q.append([i,j-1])
        