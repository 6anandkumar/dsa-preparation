#Leetcode: 407 - Incomplete
def trapRainWater(heightMap: list) -> int:
    if(len(heightMap)<=2 or len(heightMap[0])<=2):
        return 0
    m = len(heightMap)
    n = len(heightMap[0])
    max_l = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(0,m):
        max_l_row = heightMap[i][0]
        for j in range(0,n):
            max_l_row = (max(max_l_row,heightMap[i][j]))
            max_l[i][j] = max_l_row
        
    max_r = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(0,m):
        max_r_row = heightMap[i][n-1]
        for j in range(n-1,-1,-1):
            max_r_row = (max(max_r_row,heightMap[i][j]))
            max_r[i][j] = max_r_row
        
    max_t = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(0,n):
        max_t_col = heightMap[0][i]
        for j in range(0,m):
            max_t[j][i] = max(max_t_col,heightMap[j][i])
            max_t_col = max(max_t_col,heightMap[j][i])

    max_b = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(0,n):
        max_b_col = heightMap[m-1][i]
        for j in range(m-1,-1,-1):
            max_b_col = max(max_b_col,heightMap[j][i])
            max_b[j][i] = max_b_col
    print("max_l",max_l)
    print("max_r",max_r)
    print("max_t",max_t)
    print("max_b",max_b)
    res = 0
    min_water = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(0,m):
        for j in range(0,n):
            min_water[i][j]=min(max_l[i][j], max_r[i][j], max_t[i][j], max_b[i][j])-heightMap[i][j]
    
    print("min_water",min_water)
    # for i in range(1,m-1):
    #     for j in range(1,n-1):
    #         res += min(max_l[i][j], max_r[i][j], max_t[i][j], max_b[i][j]) - heightMap[i][j]
    return res


# print(trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))