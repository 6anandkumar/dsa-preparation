from heapq import heapify,heappush as push, heappop as pop
def connectRopes(arr) :
    heap = []
    heapify(heap)
    for i in arr:
        push(heap,i)

    cost = 0
    while len(heap)>1:
        s1 = pop(heap)
        s2 = pop(heap)
        cost += s1 + s2
        push(heap,s1+s2)

    return cost

print(connectRopes([1,2,3,4,5]))
print(connectRopes([4,3,2,6]))