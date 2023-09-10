import math
def MinimumElementLong(arr: list,el: int)->int:
    if(len(arr)==1):
        return abs(arr[0]-el)
    start = 0
    end = len(arr)-1
    res = math.inf
    while(start <= end):
        mid = math.floor(start + (end-start)/2)
        # if(arr[mid]==el):
        #     return 0
        res = min(res,abs(arr[mid]-el))
        if((mid>0 and abs(arr[mid]-el) < abs(arr[mid-1]-el)) and (mid<len(arr)-1 and abs(arr[mid]-el) < abs(arr[mid+1]-el))):
            res = min(res,abs(arr[mid]-el))
            return res
        if((mid==0 and mid<len(arr)-1 and abs(arr[mid]-el) < abs(arr[mid+1]-el))):
            res = min(res,abs(arr[mid]-el))
            return res
        if(mid==len(arr)-1 and mid>0 and abs(arr[mid]-el) < abs(arr[mid-1]-el)):
            res = min(res,abs(arr[mid]-el))
            return res
        if(mid>0 and abs(arr[mid-1]-el)<=res):
            end=mid-1
        elif(mid<len(arr)-1 and abs(arr[mid+1]-el)<=res):
            start = mid+1
    return res


def MinimumElement(arr: list,el: int)->int:
    if(len(arr)==1):
        return abs(arr[0]-el)
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = math.floor(start + (end-start)/2)
        if(arr[mid]==el):
            return 0
        if(arr[mid]<el):
            start=mid+1
        elif(arr[mid]>el):
            end=mid-1
    
    return min(abs(arr[start]-el), abs(arr[end]-el))




print(MinimumElement([1,3,8,10,15],12))
print(MinimumElement([1,3,8,10,12,15],12))
print(MinimumElement([12],12))
print(MinimumElement([1],12))
print(MinimumElement([1,3,8,10,12,15],1))
print(MinimumElement([1,3,8,10,12,15],15))