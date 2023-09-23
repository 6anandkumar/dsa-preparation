def sumIndicesWithKSetBits( nums: list, k: int) -> int:
    res = 0
    for i in range(len(nums)):
        b = i
        set_bits=0
        while(b!=0):
            if(b&1!=0):
                set_bits+=1
            b=b>>1
        if(set_bits==k):
            res+=nums[i]
                
    return res

print(sumIndicesWithKSetBits([5,10,1,5,2],1))