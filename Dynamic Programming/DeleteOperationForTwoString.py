#Leetcode: 583
def minDistance(x: str, y: str) -> int:
    n = len(x)
    m = len(y)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return (n-dp[-1][-1])+(m-dp[-1][-1])