#Leetcode: 779
#2 solutions:
def kthGrammar(n: int, k: int) -> int:
    #Solution 1:
    if(n==1):
        return 0
    prev_k = k/2 if(k%2==0) else (k+1)/2
    last_symbol = kthGrammar(n-1,prev_k)
    if(k%2==0):
        if(last_symbol == 1):
            return 0
        else:
            return 1
    else:
        if(last_symbol == 1):
            return 1
        else:
            return 0
    #Solution 2:
    # if(n==1 and k==1):
    #     return 0
    # mid = int(pow(2,n-1)/2)
    # if(k <= mid):
    #     return self.kthGrammar(n-1, k)
    # else:
    #     return 1 if self.kthGrammar(n-1, k-mid) == 0 else 0