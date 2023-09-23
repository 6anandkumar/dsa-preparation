#Leetcode:1143
def longestCommonSubsequence(text1: str, text2: str) -> int:
    n = len(text1)
    m = len(text2)
    # Recursive Solution:
    # mem = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    # return solve(text1,text2,n,m,mem)
    
    #Tabular Solution:
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i]=0
    for i in range(n+1):
        dp[i][0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(text1[i-1] == text2[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
def solve(x,y,n,m,mem):
    if(n==0 or m==0):
        return 0
    if(mem[n][m]!=-1):
        return mem[n][m]
    if(x[n-1] == y[m-1]):
        mem[n][m] = 1 + solve(x,y,n-1,m-1,mem)
        return mem[n][m]
    else:
        mem[n][m] = max(solve(x,y,n-1,m,mem),solve(x,y,n,m-1,mem))
        return mem[n][m]