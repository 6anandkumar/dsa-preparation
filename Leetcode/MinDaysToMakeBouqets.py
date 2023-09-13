import math
#Leetcode: 1482
def minDays(bloomDay, m: int, k: int) -> int:
    if(len(bloomDay) == 0 or len(bloomDay)<m*k):
        return -1
    start = min(bloomDay)
    end = max(bloomDay)
    res = -1
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        if(isValid(bloomDay,mid,m,k)):
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res
    
def isValid(arr,days,m,k):
    flowers = 0
    bouqets = m
    for i in range(len(arr)):
        if(arr[i]<=days):
            flowers += 1
        else:
            flowers = 0
        if(flowers == k):
            bouqets -= 1
            flowers = 0
        if(bouqets == 0):
            return True
    return False

print(minDays([1,10,3,10,2],3,1))