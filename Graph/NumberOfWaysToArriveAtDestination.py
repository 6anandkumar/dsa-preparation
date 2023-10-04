#Leetcode:1976
from typing import List
from heapq import heappush as push,heappop as pop
import math
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i,j,c in roads:
            adj[i].append((j,c))
            adj[j].append((i,c))
        
        src=0
        dst=n-1
        q=[]
        time = [math.inf for _ in range(n)]
        ways = [0 for _ in range(n)]
        # q-> {time,node}
        push(q, (0,src))
        time[src]=0
        ways[src]=1
        while(q):
            # print(q)
            t,k = pop(q)
            for e,w in adj[k]:
                if(t+w<=time[e]):
                    if(t+w < time[e]):
                        ways[e]=ways[k]
                        push(q, (t+w,e))
                    else:
                        ways[e] += ways[k]
                    time[e] = t+w
        # print(res)
        return ways[dst]%(10**9 + 7)