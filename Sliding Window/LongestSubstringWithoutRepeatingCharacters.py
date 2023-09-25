#Leetcode 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i,j=0,0
        d={}
        res = 0
        while(j<=n-1):
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            if(len(d) == j-i+1):
                res = max(res,j-i+1)
            elif(len(d) < j-i+1):
                while(len(d)!=j-i+1):
                    d[s[i]] -= 1
                    if(d[s[i]] == 0):
                        del d[s[i]]
                    i+=1
            j+=1
        return res

