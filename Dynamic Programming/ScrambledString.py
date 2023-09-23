#Leetcode: 87
#Memoize using a dictionary d[(a,b)]=flag
def isScramble( s1: str, s2: str) -> bool:
    return solve(s1,s2)
def solve( a, b):
    # print("a,b:",a,b)
    if(a==b):
        return True
    x=len(a)
    if(x<=1):
        return False
    flag = False
    for i in range(1,x):
        swapped = solve(a[:i],b[x-i:]) and solve(a[i:],b[:x-i])
        not_swapped = solve(a[:i],b[:i]) and solve(a[i:],b[i:])
        # print("swapped:",(a[:i],b[x-i:]),"and",(a[i:],b[:x-i]),swapped)
        # print("not_swapped:",(a[:i],b[:i]),"and",(a[i:],b[i:]),not_swapped)
        if(swapped or not_swapped):
            flag = True
            break
    return flag

print(isScramble("great","rgeat"))