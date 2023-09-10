import math
#Leetcode 1095
class MountainArray:
    arr = []
    def __init__(self,arr) -> None:
        self.arr = arr
    def get(self, index: int) -> int:
        return self.arr[index]
    def length(self) -> int:
        return len(self.arr)

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.getPeakIndex(mountain_arr)
        if(mountain_arr.get(peak)==target):
            return peak
        left_check = self.bsInAscArray(mountain_arr,0,peak-1,target)
        if(left_check!=-1):
            return left_check
        right_check = self.bsInDscArray(mountain_arr,peak+1,mountain_arr.length()-1,target)
        return right_check

    def bsInAscArray(self,arr,st,ed,target):
        start = st
        end = ed
        while(start<=end):
            mid = math.floor(start+(end-start)/2)
            arr_mid = arr.get(mid)
            if(arr_mid==target):
                return mid
            if(target>arr_mid):
                start=mid+1
            elif(target<arr_mid):
                end=mid-1
        return -1

    def bsInDscArray(self,arr,st,ed,target):
        start = st
        end = ed
        while(start<=end):
            mid = math.floor(start+(end-start)/2)
            arr_mid = arr.get(mid)
            if(arr_mid==target):
                return mid
            if(target>arr_mid):
                end=mid-1
            elif(target<arr_mid):
                start=mid+1
        return -1

    def getPeakIndex(self,arr):
        start = 0
        end = arr.length()-1
        while(start <= end):
            mid = math.floor(start + (end-start)/2)
            arr_mid = arr.get(mid)
            if(mid!=0):
                arr_mid_l = arr.get(mid-1)
            if(mid!=arr.length()-1):
                arr_mid_r = arr.get(mid+1)
            if(mid != 0 and mid!=arr.length()-1 and arr_mid>arr_mid_l and arr_mid>arr_mid_r):
                return mid
            if(arr_mid_r>arr_mid):
                start=mid+1
            elif(arr_mid_l>arr_mid):
                end=mid-1
        return -1

arr = MountainArray([1,2,3,4,5,3,1])
print(arr.findInMountainArray(3,arr))