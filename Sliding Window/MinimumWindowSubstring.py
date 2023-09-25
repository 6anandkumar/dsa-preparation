class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        d={}
        c=0
        for i in t:
            if i not in d:
                d[i] = 1
                c+=1
            else:
                d[i] += 1
        i,j=0,0
        res_count = n+2
        res_i,res_j = -1,-1
        while(j<=n-1):
            if s[j] in d:
                d[s[j]] -= 1
                if(d[s[j]] == 0):
                    c-=1
            if(c==0):
                if(j-i+1 < res_count):
                    res_count = j-i+1
                    res_i,res_j=i,j
                while(c==0):
                    if s[i] in d:
                        d[s[i]] += 1
                        if(d[s[i]]>0):
                            c+=1
                    i+=1
                    if(c==0 and j-i+1 < res_count):
                        res_count = j-i+1
                        res_i,res_j=i,j
            j+=1
        res = ""
        if(res_i != -1):
            for i in range(res_i,res_j+1):
                res += s[i]
        return res
