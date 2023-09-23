def maxProfit(wts,vals,cap):
    n = len(wts)
    c = cap
    dp = [[-1 for i in range(c+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(c+1):
        dp[0][i] = 0
    
    for i in range(1,n+1):
        for j in range(1,c+1):
            if(wts[i-1]<=j):
                dp[i][j] = max(vals[i-1]+dp[i-1][j-wts[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[-1][-1]

print(maxProfit([4,5,1],[1,2,3],4))
print(maxProfit([4],[10],4))
