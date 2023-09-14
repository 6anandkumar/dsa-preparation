def permutation_of_space(s):
    res = []
    s = list(s)
    i = s.pop(0)
    solve(s,res,[i])
    return res

def solve(s,res,op):
    if(len(s)==0):
        res.append("".join(op))
        return
    s = s.copy()
    i = s.pop(0)
    with_space = op + [" "] + [i]
    without_space = op + [i]
    solve(s,res,with_space)
    solve(s,res,without_space)
    return

print(permutation_of_space("abc"))