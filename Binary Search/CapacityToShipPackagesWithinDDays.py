import math
def shipWithinDays(weights: list, days: int) -> int:
    start = max(weights)
    end = sum(weights)-start
    res = -1
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        if(isValid(weights,mid,days)):
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res

def isValid(arr,mid,days):
    days_required = 1
    sum_of_weights = 0
    for i in range(len(arr)):
        sum_of_weights += arr[i]
        if(sum_of_weights > mid):
            days_required += 1
            sum_of_weights = arr[i]
        if(days_required>days):
            return False
    return True

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10],1))