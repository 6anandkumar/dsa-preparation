#Leetcode: 904
class Solution:
    def totalFruit(self, fruits: list) -> int:
        n = len(fruits)
        i,j=0,0
        d={}
        res = 0
        sm = 0
        while(j<=n-1):
            if(fruits[j] not in d):
                d[fruits[j]] = 1
            else:
                d[fruits[j]] += 1
            sm += 1
            if(len(d)<=2):
                res = max(res,sm)
                j+=1
            # elif(len(d)<2):
            #     j+=1
            else:
                while(not (len(d)<=2)):
                    d[fruits[i]] -= 1
                    sm-=1
                    if(d[fruits[i]] == 0):
                        del d[fruits[i]]
                    i+=1
                if(len(d)<=2):
                    res = max(res,sm)
                j+=1
        return res
            