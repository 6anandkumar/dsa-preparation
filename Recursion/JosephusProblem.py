def findTheWinner(n: int, k: int) -> int:
    start = 0
    arr = [x+1 for x in range(n)]
    res = solve(start,k-1,arr)
    return res
def solve(start,k,arr):
    if(len(arr)==1):
        return arr[0]
    out = (start+k)%len(arr)
    arr.pop(out)
    start = out
    res = solve(start,k,arr)
    return res