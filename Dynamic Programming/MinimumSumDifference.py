import math
def minimumDifference(nums: list) -> int:
    n = len(nums)
    sum_nums = sum(nums)
    c = math.ceil(sum_nums/2)
    dp = [[-1 for _ in range(c+1)] for _ in range(n+1)]
    for i in range(c+1):
        dp[0][i] = 0
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1,n+1):
        for j in range(1,c+1):
            if(nums[i-1]<=c):
                dp[i][j] = max(nums[i-1] + dp[i-1][j-nums[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return abs(sum_nums-dp[-1][-1])

# print(minimumDifference([3,9,7,3]))
print(minimumDifference([2,-1,0,4,-2,-9]))
# print(minimumDifference([-36,36]))