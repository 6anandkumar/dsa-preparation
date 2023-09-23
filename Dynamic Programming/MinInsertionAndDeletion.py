#Find the min number of insertion and deletion required to convert string x to string y
def minInsertionDeletion(x,y):
    n = len(x)
    m = len(y)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    len_subseq = dp[-1][-1]
    deletions = n-len_subseq
    insertions = m-len_subseq
    return [insertions,deletions]