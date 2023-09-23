import math
def coinChange(coins: list, amount: int) -> int:
    n = len(coins)
    t = amount
    dp = [[-1 for _ in range(t+1)] for _ in range(n+1)]
    for i in range(t+1):
        dp[0][i] = math.inf
    for j in range(n+1):
        dp[j][0] = 0
    for i in range(1,n+1):
        for j in range(1,t+1):
            if(coins[i-1]<=j):
                dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1] if dp[-1][-1]!=math.inf else -1