import math
class Solution:
    d={}
    def superEggDrop(self, k: int, n: int) -> int:
        self.d={}
        return self.solve(k,n)
    
    def solve(self,eggs,n):
        if((eggs,n) in self.d):
            return self.d[(eggs,n)]
        if(n==0 or n==1):
            return n
        if(eggs==1):
            return n
        ans = math.inf
        start=1
        end=n-1
        while(start<=end):
            mid = math.floor(start + (end-start)/2)
            breaks = self.solve(eggs-1,mid-1)
            not_breaks = self.solve(eggs,n-mid)
            temp = 1+max(breaks,not_breaks)
            if(breaks > not_breaks):
                end = mid-1
            else:
                start = mid+1
            ans = min(ans,temp)
        self.d[(eggs,n)] = ans
        return ans