from heapq import heapify,heappush as push, heappop as pop
#Leetcode: 973
def kClosest(points: list, k: int) -> list:
    heap =[]
    heapify(heap)
    res = []
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        distance = (x**2 + y**2)**0.5
        push(heap,(-distance,points[i]))
        if(len(heap)>k):
            pop(heap)
    while(heap):
        res.append(pop(heap)[1])
    return res