import math
def BinarySearchOnAgnosticArray(arr: list,el: int)->int:
    start = 0
    end = len(arr)-1
    order = 0 if(len(arr)>1 and (arr[1]>arr[0])) else 1 #Assuming no repeated elements
        
    while(start <= end):
        mid = math.floor(start + (end-start)/2)
        if(el == arr[mid]):
            return mid
        elif(el > arr[mid]):
            if(not order):
                start = mid+1
            else:
                end = mid-1
        else:
            if(not order):
                end = mid-1
            else:
                start = mid+1
    return -1

print(BinarySearchOnAgnosticArray([1,2,3,4,5,6,7,8,9],2))
print(BinarySearchOnAgnosticArray([1,2,3,4,5,6,7,8,9],9))
print(BinarySearchOnAgnosticArray([1,2,3,4,5,6,7,8,9],5))
print(BinarySearchOnAgnosticArray([1,2,3,4,5,6,7,8,9],10))
print(BinarySearchOnAgnosticArray([9, 8, 7, 6, 5, 4, 3, 2, 1],2))
print(BinarySearchOnAgnosticArray([9, 8, 7, 6, 5, 4, 3, 2, 1],9))
print(BinarySearchOnAgnosticArray([9, 8, 7, 6, 5, 4, 3, 2, 1],5))
print(BinarySearchOnAgnosticArray([9, 8, 7, 6, 5, 4, 3, 2, 1],10))