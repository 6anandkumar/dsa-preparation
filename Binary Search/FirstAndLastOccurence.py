import math
def FirstOccurence(arr: list,el: int)->int:
    if(not len(arr)):
        return -1
    elif(len(arr)==1):
        if(arr[0] == el):
            return 0
        else:
            return -1
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = math.floor(start + (end-start)/2)
        if(el == arr[mid]):
            if(mid-1 > -1 and arr[mid-1] < el):
                return mid
            elif(mid-1 > -1 and arr[mid-1] == el):
                end = mid-1
            else:
                return mid
        elif(el > arr[mid]):
            start = mid+1
        else:
            end = mid-1
    return -1

def LastOccurence(arr: list,el: int)->int:
    if(not len(arr)):
        return -1
    elif(len(arr)==1):
        if(arr[0] == el):
            return 0
        else:
            return -1
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = math.floor(start + (end-start)/2)
        if(el == arr[mid]):
            if(mid+1 < len(arr) and arr[mid+1] > el):
                return mid
            elif(mid+1 < len(arr) and arr[mid+1] == el):
                start = mid+1
            else:
                return mid
        elif(el > arr[mid]):
            start = mid+1
        else:
            end = mid-1
    return -1

print(FirstOccurence([2,4,10,10,10,18,20],10))
print(LastOccurence([2,4,10,10,10,18,20],10))
print(LastOccurence([2,2],2))
print(FirstOccurence([2,2],2))
print(FirstOccurence([],2))