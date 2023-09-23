#Leetcode:1547
#Incomplete
def minCost(cuts,cap):
    # t =  n
    # n = len(cuts)
    # dp = [[-1 for _ in range(t+1)] for _ in range(n+1)]
    # for i in range(t+1):
    #     dp[0][t] = t
    # for i in range(n+1):
    #     dp[i][0] = 0
    # for i in range(1,n+1):
    #     for j in range(1,t+1):
    #         if(cuts[i-1]<=j):
    #             dp[i][j] = min(j+dp[i-1][j-cuts[i-1]],dp[i-1][j])
    #         else:
    #             dp[i][j] = dp[i-1][j]
    # return dp[-1][-1]