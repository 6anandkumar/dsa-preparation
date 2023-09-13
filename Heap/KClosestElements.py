#Leetcode 658
from heapq import heapify,heappush as push,heappop as pop
def findClosestElements(arr: list, k: int, x: int) ->list:
    heap = []
    heapify(heap)
    res = []
    for i in range(len(arr)):
        push(heap,(abs(arr[i]-x),arr[i]))
        # if(len(heap)>k):
        #     pop(heap)
    while(k):
        res.append(pop(heap)[1])
        k-=1
    res.sort()
    return res

print(findClosestElements([1,2,3,4,5],4,3))