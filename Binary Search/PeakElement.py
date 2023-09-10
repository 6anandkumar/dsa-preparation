import math
#leetcode 162
def findPeakElement(nums: list) -> int:
    if(len(nums)==1):
        return 0
    start  = 0
    end = len(nums)-1
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        if(mid==0 and mid<len(nums)-1 and nums[mid]>nums[mid+1]):
            return mid
        if(mid==len(nums)-1 and mid>0 and nums[mid]>nums[mid-1]):
            return mid
        if(nums[mid] > nums[mid-1] and nums[mid]>nums[mid+1]):
            return mid
        if(mid==0 and mid<len(nums)-1):
            start = mid+1
        elif(mid==len(nums)-1 and mid>0):
            end = mid-1
        elif(nums[mid] < nums[mid-1]):
            end=mid-1
        elif(nums[mid] < nums[mid+1]):
            start = mid+1
    return -1