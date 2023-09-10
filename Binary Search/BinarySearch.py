import math
def BinarySearch(arr: list,el: int)->int:
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = math.floor(start + (end-start)/2)
        if(el == arr[mid]):
            return mid
        elif(el > arr[mid]):
            start = mid+1
        else:
            end = mid-1
    return -1

print(BinarySearch([1,2,3,4,5,6,7,8,9],2))
print(BinarySearch([1,2,3,4,5,6,7,8,9],9))
print(BinarySearch([1,2,3,4,5,6,7,8,9],5))
print(BinarySearch([1,2,3,4,5,6,7,8,9],10))