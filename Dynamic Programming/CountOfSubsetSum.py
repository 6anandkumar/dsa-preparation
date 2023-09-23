def countSubsetSum(nums,target):
    n = len(nums)
    t = target
    dp = [[-1 for i in range(t+1)] for j in range(n+1)]
    for i in range(t+1):
        dp[0][i] = 0
    for j in range(n+1):
        dp[j][0] = 1
    for i in range(1,n+1):
        for j in range(1,t+1):
            if(nums[i-1]<=j):
                k = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                dp[i][j] = k
            else:
                k = dp[i-1][j]
                dp[i][j] = k
    return dp[-1][-1]
        
    

print(countSubsetSum([2,3,5,6,8,10],10))    #3
print(countSubsetSum([1,2,3,3],6))    #3
print(countSubsetSum([1,1,1,1],1))    #4
print(countSubsetSum([3,3,3,3],6))    #6
print(countSubsetSum([1,1,2,3],4))    #3