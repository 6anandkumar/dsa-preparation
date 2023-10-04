#Leetcode: 787

#This solution is correct but gives TLE as the number of nodes are visited again and again
#This is modified Dijkstra's Algo where not using dist array to store stops but pushing into queue
from heapq import heapify,heappush as push,heappop as pop
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for i in flights:
            f,t,p = i[0],i[1],i[2]
            adj[f].append((t,p))
        q = []
        push(q, (0,src,0))

        while(q):
            c,i,d = pop(q)
            if(i==dst):
                return c
            for e,w in adj[i]:
                if(d+1<=k+1):
                    push(q, (c+w,e,d+1))
        return -1

#Working Solution
# This is modified Dijkstra's Algo where using priority queue is maintained for stops instead of price
# Normal Queue can also be used instead of Priority Queue
from collections import deque
import math
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for i in flights:
            f,t,p = i[0],i[1],i[2]
            adj[f].append((t,p))
        
        q = deque()
        cost = [math.inf for _ in range(n)]
        q.append((0,src,0))
        cost[src]=0

        res=math.inf
        while(q):
            s,i,c = q.popleft()
            if i==dst:
                res = min(res,c)
            if(s>k):
                continue
            for e,w in adj[i]:
                if(c+w < cost[e] and s<=k):
                    cost[e] = c+w
                    q.append((s+1,e,c+w))
        return res if res != math.inf else -1