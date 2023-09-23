def findMaxProfit(wts, vals, capacity):
    mem = [[-1 for i in range(len(wts)+1)] for j in range(capacity+1)]
    res = solve(wts, vals, capacity,mem)
    return res
    
def solve(wts, vals, capacity,mem):
    weights = wts.copy()
    values = vals.copy()
    if(len(weights)==0 or len(values)==0):
        return 0
    c,l = capacity,len(wts)
    if(mem[c][l] != -1):
        return mem[c][l]
    w = weights.pop()
    v = values.pop()
    if(w<=capacity):
        mem[c][l] =  max(solve(weights,values,capacity-w,mem)+v,solve(weights,values,capacity,mem))
        return mem[c][l]
    else:
        mem[c][l] = solve(weights,values,capacity,mem)
        return mem[c][l]

print(findMaxProfit([4,5,1],[1,2,3],4))

    