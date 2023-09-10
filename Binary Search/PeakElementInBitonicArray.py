import math
#leetcode 852
def peakIndexInMountainArray(arr: list) -> int:
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = math.floor(start + (end-start)/2)
        if(mid != 0 and mid!=len(arr)-1 and arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
            return mid
        if(arr[mid+1]>arr[mid]):
            start=mid+1
        elif(arr[mid-1]>arr[mid]):
            end=mid-1
    return -1