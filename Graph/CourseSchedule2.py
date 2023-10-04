#Leetcode: 210
from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj[b].append(a)
        indegree = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            for e in adj[i]:
                indegree[e] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        topoSort = []
        self.bfs(q,indegree,adj,topoSort)
        if(len(topoSort)<numCourses):
            return []
        return topoSort
        
    def bfs(self,q,indegree,adj,res):
        while(q):
            k = q.popleft()
            res.append(k)
            for e in adj[k]:
                indegree[e] -= 1
                if not indegree[e]:
                    q.append(e)