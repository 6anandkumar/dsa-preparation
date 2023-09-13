#Leetcode 347
from heapq import heapify,heappush as push,heappop as pop
from collections import defaultdict
def topKFrequent(nums: list, k: int) -> list:
    heap = []
    heapify(heap)
    d=defaultdict(int)
    res=[]
    for i in range(len(nums)):
        d[nums[i]]+=1
    for i in d:
        push(heap,(d[i],i))
        if(len(heap)>k):
            pop(heap)
    while(heap):
        res.append(pop(heap)[1])
    return res