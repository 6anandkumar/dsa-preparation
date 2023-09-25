from collections import deque
import math
class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        n = len(nums)
        q = deque()
        i=0
        j=0
        res = []
        while(j<=n-1):
            if(j-i+1!=k):
                if(j==0 and nums[j]<0):
                    q.append(j)
                j+=1
                if(nums[j]<0):
                    q.append(j)
            else:
                if(len(q)==0):
                    res.append(0)
                else:
                    res.append(nums[q[0]])
                if(q and q[0]==i):
                    q.popleft()
                j += 1
                if(j<n and nums[j]<0):
                    q.append(j)
                i += 1
        return res

obj = Solution()
print(obj.maxSlidingWindow([1,3,-1,-3,5,3,6,-7],3))