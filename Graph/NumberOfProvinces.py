#Leetcode: 547
#Simplified problem statement: find the number of disconnected groups
from typing import List
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected[0])
        vis = [0 for _ in range(n)]
        root = 0
        res = 0
        for i in range(n):
            if vis[i] != 1:
                res += 1
                self.bfs(root,isConnected,vis,n)
        return res
    def bfs(self,node,adj,vis,n):
        q = deque()
        q.append(node)
        vis[node] = 1
        while(q):
            k = q.popleft()
            for i in range(n):
                if adj[k][i] == 1:
                    if vis[i] != 1:
                        vis[i] = 1
                        q.append(i)
        
a = Solution()               
print(a.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))   #2
print(a.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))   #3