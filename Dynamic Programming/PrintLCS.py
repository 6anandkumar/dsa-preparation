def printLCS(text1,text2):
    n = len(text1)
    m = len(text2)
    dp = [[[-1,""] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i]=[0,""]
    for i in range(n+1):
        dp[i][0]=[0,""]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(text1[i-1] == text2[j-1]):
                dp[i][j] = [1 + dp[i-1][j-1][0],dp[i-1][j-1][1]+text1[i-1]]
            else:
                dp[i][j] = [dp[i-1][j][0],dp[i-1][j][1]] if(dp[i-1][j][0] > dp[i][j-1][0]) else [dp[i][j-1][0],dp[i][j-1][1]]#max(dp[i-1][j][0], dp[i][j-1][0])
    return dp[-1][-1][1]

print(printLCS("abcdaf","acbcf"))


def printLCS2(x,y):
    n = len(x)
    m = len(y)
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i]=0
    for i in range(n+1):
        dp[i][0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    a,b=n,m
    res = ""
    while(a and b):
        if(x[a-1] == y[b-1]):
            res += x[a-1]
            a-=1
            b-=1
        elif(dp[a][b] == dp[a-1][b]):
            a-=1
        elif(dp[a][b] == dp[a][b-1]):
            b-=1
    return res[::-1]

print(printLCS2("abcdaf","acbcf"))