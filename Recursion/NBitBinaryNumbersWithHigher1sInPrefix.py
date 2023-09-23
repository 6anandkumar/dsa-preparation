#Print all N bit binary numbers with 1's more than 0's for any prefix (here the 1's and 0's can also be equal)
def nBitNumbers(n):
    ones = 0
    zeroes = 0
    res = []
    solve(ones,zeroes,res,"",n)
    return res
def solve(ones,zeroes,res,op,n):
    if(len(op)==n):
        res.append(op)
        return
    if(ones>zeroes):    # Do (ones>zeroes) if 1's and 0's can be equal as well, else do (ones>zeroes+1) if 1's are strictly greater than 0's
        solve(ones+1,zeroes,res,op+"1",n)
        solve(ones,zeroes+1,res,op+"0",n)
    else:
        solve(ones+1,zeroes,res,op+"1",n)
    return

print(nBitNumbers(4))