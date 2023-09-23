def countSubsets(nums,target):
    if abs(target) > sum(nums): return 0
    diff = target
    total_sum = sum(nums)
    t = (diff+total_sum)/2
    if(int((diff+total_sum)/2) != t):
        return 0
    t=int(t)
    n = len(nums)
    dp = [[-1 for i in range(t+1)] for j in range(n+1)]
    for i in range(t+1):
        dp[0][i] = 0
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(t+1):
            if(nums[i-1]<=j):
                dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

print(countSubsets([1,1,2,3],1))    #3
print(countSubsets([0,0,0,0,0,0,0,0,1],1))    #256
    