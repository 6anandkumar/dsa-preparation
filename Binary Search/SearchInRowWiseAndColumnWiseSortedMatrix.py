#Leetcode: 74,240
def searchMatrix(matrix: list, target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    a = 0
    b = m-1
    while(a>=0 and a<=n-1 and b>=0 and b<=m-1):
        if(matrix[a][b]==target):
            return True
        if(matrix[a][b]>target):
            b-=1
        elif(matrix[a][b]<target):
            a+=1
    return False