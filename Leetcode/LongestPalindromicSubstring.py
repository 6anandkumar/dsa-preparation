def longestPalindrome(x: str) -> str:
    y = x[::-1]
    if(x==y):
        return x
    n = len(x)
    m=n
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    possible_palindromes = []
    mx_len=0
    u,v=0,0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
                if(dp[i][j] > mx_len):
                    mx_len = dp[i][j]
                    u,v=i,j
                if(dp[i][j] > 1):
                    possible_palindromes.append([i,j])
    res=""
    u_temp,v_temp=u,v
    while((u and v) and x[u-1] == y[v-1]):
        res+=x[u-1]
        u-=1
        v-=1
    
    if(res == res[::-1]):
        return res
    res=""
    for a,b in possible_palindromes:
        if(a==u_temp and b==v_temp):
            continue
        substr = ""
        while((a and b) and x[a-1] == y[b-1]):
            substr+=x[a-1]
            a-=1
            b-=1
        if(substr == substr[::-1] and len(substr)>len(res)):
            res = substr
    return res if len(res) > 0 else x[0]