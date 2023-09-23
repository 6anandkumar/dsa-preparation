d={}
def evaluateToTrue(s):
    return solve(s,True)
def solve(s,isTrue):
    n = len(s)
    if(n==0):
        return 0
    if(n==1):
        if isTrue: return 1 if s[0]=="T" else 0
        else: return 1 if s[0]=="F" else 0
    if((s,isTrue) in d):
        return d[(s,isTrue)]
    ans = 0
    for i in range(1,n-1,2):
        left_true = solve(s[:i],True)
        right_true = solve(s[i+1:],True)
        left_false = solve(s[:i],False)
        right_false = solve(s[i+1:],False)
        op = s[i]
        if(op=="&"):
            if(isTrue):
                ans += (left_true*right_true)
            else:
                ans += (left_false*right_false) + (left_true*right_false) + (left_false*right_true)
        elif(op=="|"):
            if(isTrue):
                ans += (left_true*right_true) + (left_true*right_false) + (left_false*right_true)
            else:
                ans += (left_false*right_false)
        elif(op=="^"):
            if(isTrue):
                ans += (left_true*right_false) + (left_false*right_true)
            else:
                ans += (left_false*right_false) + (left_true*right_true)
    d[(s,isTrue)] = ans
    print(ans,n)
    return ans

# print(evaluateToTrue("t|f&t^f"))
# print(evaluateToTrue("t^f&t"))
# print(evaluateToTrue("t|t&f^t"))
print(evaluateToTrue("T|F^F&T|F^F^F^T|T&T"))

# 35
# T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F