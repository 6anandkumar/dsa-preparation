#Leetcode: 784
def letterCasePermutation(s: str) -> list:
    s = list(s)
    res = []
    solve(s,res,[])
    return res
def solve(ss,res,opt):
    s = ss.copy()
    op = opt.copy()
    if(len(s)==0):
        res.append("".join(op))
        return
    el = s.pop(0)
    caps = op.copy()
    lows = op.copy()
    if(el.isnumeric()):
        caps += [el]
        solve(s,res,caps)
    else:
        caps += [el.upper()]
        lows += [el.lower()]
        solve(s,res,caps)
        solve(s,res,lows)
    return