#Leetcode: 416
def canPartition(nums):
    sum_nums = sum(nums)
    if(sum_nums%2 != 0):
        return False
    cap = int(sum_nums/2)
    mem = [[-1 for i in range(len(nums)+1)] for j in range(cap+1)]
    return True if solve(nums,cap,mem) else False
def solve(ns,cap,mem):
    nums = ns.copy()
    if(len(nums)>=0 and cap==0):
        return 1
    elif(len(nums)==0):
        return 0
    c,l = cap,len(nums)
    if(mem[c][l]!=-1):
        return mem[c][l]
    el = nums.pop()
    if(el<=cap):
        mem[c][l] = max(solve(nums,cap-el,mem), solve(nums,cap,mem))
        return mem[c][l]
    else:
        mem[c][l] = solve(nums,cap,mem)
        return mem[c][l]
    
def canPartition_bottom_up(nums: list) -> bool:
    sum_nums = sum(nums)
    if(sum_nums%2 != 0):
        return False
    cap = int(sum_nums/2)
    n = len(nums)
    dp = [[-1 for i in range(cap+1)] for j in range(n+1)]
    for i in range(cap+1):
        dp[0][i] = 0
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,cap+1):
            if(nums[i-1]<=j):
                dp[i][j] = max(dp[i-1][j-nums[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

print(canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))