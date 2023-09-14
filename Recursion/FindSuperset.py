def subsets(nums: list) -> list:
    if(len(nums)==1):
        return [[],nums]
    res = []
    superset = find_subsets(nums,res,[])
    return superset

def find_subsets(nums,res,op):
    if(not len(nums)):
        res.append(op)
        return
    ip = nums.copy()
    e = ip.pop()
    left = op.copy()
    right = op.copy()
    right.append(e)
    find_subsets(ip,res,left)
    find_subsets(ip,res,right)
    return res

print(subsets([1,2]))