def partition(s: str):
    i=0
    j=len(s)
    return solve(s,i,j)
def solve(s,i,j):
    ss = s[i:j]
    if not ss: return [[]]
    item = []
    for k in range(i,j):
        left = s[i:k+1]
        if(left == left[::-1]):
            right = solve(s,k+1,j)
            for p in right:
                item.append([left] + p)
    return item

def partition2( s):
    if not s: return [[]]
    ans = []
    for i in range(1, len(s) + 1):
        if s[:i] == s[:i][::-1]:  # prefix is a palindrome
            for suf in partition(s[i:]):  # process suffix recursively
                ans.append([s[:i]] + suf)
    return ans
print(partition("abba"))