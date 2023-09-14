#Leetcode: 22
def generateParenthesis(n: int) -> list:
    opn = n
    close = n
    res = []
    solve(opn,close,res,"")
    return res

def solve(opn,close,res,op):
    if(opn == 0 and close == 0):
        res.append(op)
        return
    if(close>opn):
        if(opn!=0):
            solve(opn-1,close,res,op+"(")
        solve(opn,close-1,res,op+")")
    else:
        solve(opn-1,close,res,op+"(")
    return