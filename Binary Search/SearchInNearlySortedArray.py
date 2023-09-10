import math
def SearchInNearlySortedArray(arr:list,el:int)->int:
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        if(el == arr[mid] or (mid > 0 and el == arr[mid-1]) or (mid < len(arr)-1 and el == arr[mid+1])):
            return mid if el==arr[mid] else mid-1 if (mid > 0 and el == arr[mid-1]) else mid+1
        elif(el < arr[mid]):
            end = mid-2
        else:
            start = mid+2
    return -1

print(SearchInNearlySortedArray([5,10,30,20,40],20))
print(SearchInNearlySortedArray([5],5))
print(SearchInNearlySortedArray([10,5],5))
print(SearchInNearlySortedArray([],5))