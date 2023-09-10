import math
def singleNonDuplicate(nums: list) -> int:
    if(len(nums)==1):
        return nums[0]
    start = 0
    end = len(nums)-1
    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        if((mid>0 and nums[mid] != nums[mid-1]) and (mid < len(nums)-1 and nums[mid] != nums[mid+1])):
            return nums[mid]
        if(mid == len(nums)-1 and mid>0 and nums[mid] != nums[mid-1]):
            return nums[mid]
        if(mid == 0 and mid<len(nums)-1 and nums[mid] != nums[mid+1]):
            return nums[mid]
        if(mid>0 and nums[mid] == nums[mid-1]):
            if((mid-1)%2 == 0):
                start = mid+1
            else:
                end = mid-1
        elif(mid < len(nums)-1 and nums[mid] == nums[mid+1]):
            if(mid%2 == 0):
                start = mid+1
            else:
                end = mid-1
    return -1

print(singleNonDuplicate([1,1,2]))
print(singleNonDuplicate([1,2,2]))
print(singleNonDuplicate([1]))