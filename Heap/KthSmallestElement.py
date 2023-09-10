from heapq import heapify,heappush as push,heappop as pop

def KthSmallestElement(arr,k):
    heap = []
    heapify(heap)
    for i in range(len(arr)):
        push(heap,-arr[i])
        if(len(heap)>k):
            pop(heap)
    return -heap[0]

print(KthSmallestElement([7,10,4,3,20,15],3))