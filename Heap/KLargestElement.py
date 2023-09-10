from heapq import heapify,heappush as push, heappop as pop

def KLargestElement(arr,k):
    heap = []
    heapify(heap)
    res = []
    for i in range(len(arr)):
        push(heap,arr[i])
        if(len(heap)>k):
            pop(heap)
    while(heap):
        res.append(pop(heap))
    return res

print(KLargestElement([7,10,4,3,20,15],3))