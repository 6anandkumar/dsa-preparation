def maxCoins(nums: list) -> int:
    return solve(nums,len(nums)-1)
def solve(nms,i):
    nums = nms.copy()
    if(i==0):
        return nums[i]
    el = nums[i]
    coins = nums[i-1]*nums[i]
    if(i!=len(nums)-1):
        coins *= nums[i+1]
    popped_nums = nums.copy()
    popped_nums.pop()
    max_coins = max(coins + solve(popped_nums,i-1),solve(nums,i-1))
    return max_coins

print(maxCoins([3,1,5,8]))