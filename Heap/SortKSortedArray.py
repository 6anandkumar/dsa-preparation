from heapq import heapify,heappush as push,heappop as pop

def sort(arr,k):
    heap = []
    heapify(heap)
    res = []
    for i in range(len(arr)):
        push(heap,arr[i])
        if(len(heap)>k+1):
            res.append(pop(heap))
    while(heap):
        res.append(pop(heap))
    
    return res

print(sort([6,5,3,2,8,10,9],3))