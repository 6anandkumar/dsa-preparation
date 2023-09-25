#Leetcode:2461
class Solution:
    def maximumSubarraySum(self, nums: list, k: int) -> int:
        n = len(nums)
        i,j=0,0
        d={}
        dis = 0
        res = 0
        sm = 0
        while(j<=n-1):
            sm += nums[j]
            if nums[j] not in d:
                d[nums[j]] = 1
                dis += 1
            else:
                d[nums[j]] += 1
            if(j-i+1<k):
                j+=1
            elif(j-i+1==k):
                if dis != k:
                    while(dis != len(d)):
                        d[nums[i]] -= 1
                        sm -= nums[i]
                        if(d[nums[i]] == 0):
                            del d[nums[i]]
                            dis -= 1
                        i+=1
                else:
                    res = max(res, sm)
                j+=1
            else:
                d[nums[i]] -= 1
                sm -= nums[i]
                if(d[nums[i]] == 0):
                    del d[nums[i]]
                    dis -= 1
                if dis == len(d) == k:
                    res = max(res, sm)
                i+=1
                j+=1
        return res
