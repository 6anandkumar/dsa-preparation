import math
def minCut( s: str) -> int:
    i=0
    j=len(s)
    mem = [-1 for _ in range(j+1)]
    return solve(s,i,j,mem)
def solve(s,i,j,mem):
    if(i>=j-1):
        return 0
    if(mem[i]!=-1):
        return mem[i]
    ss = s[i:j]
    if(ss==ss[::-1]):
        mem[i] = 0
        return 0
    res = math.inf
    for k in range(i,j-1):
        ss = s[i:k+1]
        if(ss==ss[::-1]):
            right = solve(s,k+1,j,mem)
            temp = 1 + right
            mem[i] = min(res,temp)
            res = mem[i]
    return res

print(minCut("abcbk"))
print(minCut("aaab"))