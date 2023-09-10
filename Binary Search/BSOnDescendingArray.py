import math
def BinarySearchOnDescendingArray(arr: list,el:int)->int:
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        if(el == arr[mid]):
            return mid
        elif(el>arr[mid]):
            end = mid-1
        else:
            start = mid+1
    return -1

print(BinarySearchOnDescendingArray([9, 8, 7, 6, 5, 4, 3, 2, 1],2))
print(BinarySearchOnDescendingArray([9, 8, 7, 6, 5, 4, 3, 2, 1],9))
print(BinarySearchOnDescendingArray([9, 8, 7, 6, 5, 4, 3, 2, 1],5))
print(BinarySearchOnDescendingArray([9, 8, 7, 6, 5, 4, 3, 2, 1],10))