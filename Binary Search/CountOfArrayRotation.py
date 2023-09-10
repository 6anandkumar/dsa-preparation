import math
def CountRotation(arr: list)->int:
    if((not len(arr))):
        return -1
    if(len(arr)==1):
        return 0
    if(len(arr)==2):
        return 0 if arr[0] <= arr[1] else 1
    start = 0
    end = len(arr)-1
    n = len(arr)
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        prev_num = arr[(mid-1+n)%n]
        next_num = arr[(mid+1)%n]
        if(arr[mid]<=prev_num and arr[mid]<=next_num):
            return n-mid    #assuming left rotation
        elif(arr[start]<=arr[end]):
            return start
        elif(not (arr[start] <= arr[mid])):
            end = mid-1
        elif(not (arr[mid] <= arr[end])):
            start = mid+1
        else:
            return 0
    return 0

def MinimumElement(arr: list)->int:
    if((not len(arr))):
        return -1
    if(len(arr)==1):
        return arr[0]
    if(len(arr)==2):
        return arr[0] if arr[0] <= arr[1] else arr[1]
    start = 0
    end = len(arr)-1
    n = len(arr)
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        prev_num = arr[(mid-1+n)%n]
        next_num = arr[(mid+1)%n]
        if(arr[mid]<=prev_num and arr[mid]<=next_num):
            return arr[mid]
        elif(arr[start]<=arr[end]):
            return arr[start]
        elif(not (arr[start] <= arr[mid])):
            end = mid-1
        elif(not (arr[mid] <= arr[end])):
            start = mid+1
        else:
            return arr[0]
    return arr[0]

# print(MinimumElement([2,5,6,8,11,12,15,18]))
print(MinimumElement([11,12,15,18,2,5,6,8]))
# print(MinimumElement([11,12,15,18,2,3,5,6,8]))
# print(MinimumElement([11]))
# print(MinimumElement([11,12]))
# print(MinimumElement([11,12,13]))
# print(MinimumElement([]))
# print(MinimumElement([2,3,1]))



