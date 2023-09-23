def findLength(x, y) -> int:
    n = len(x)
    m = len(y)
    res = 0
    dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i] = 0
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                res = max(res,dp[i][j])
            else:
                dp[i][j] = 0
    
    return res

def findLength_slightly_shorter(x,y) -> int:
    n = len(x)
    m = len(y)
    res = 0
    dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                res = max(res,dp[i][j])
    
    return res