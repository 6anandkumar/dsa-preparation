def maxSum(arr,k):
    n = len(arr)
    i=0
    if(n<k):
        return 0
    j = i+k-1
    sm = sum(arr[:j+1])
    res = sm
    while(j<n-1):
        j+=1
        sm += arr[j]
        sm -= arr[i]
        i += 1
        res = max(res,sm)
    return res

print(maxSum([-2,1,-3,4,-1,2,1,-5,4],4))
        
        