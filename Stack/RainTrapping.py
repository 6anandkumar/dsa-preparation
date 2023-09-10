def RainTrapping(heights: list)->int:
    mxl = [heights[0]]
    for i in range(1,len(heights)):
        mxl.append(max(mxl[-1],heights[i]))
    mxr = [heights[-1]]
    for i in range(len(heights)-2,-1,-1):
        mxr.append(max(mxr[-1],heights[i]))
    mxr.reverse()
    res = 0
    for i in range(len(heights)):
        res += min(mxl[i],mxr[i])-heights[i]
    return res

print(RainTrapping([0,1,0,2,1,0,1,3,2,1,2,1]))
print(RainTrapping([3,0,0,2,0,4]))
print(RainTrapping([4,2,0,3,2,5]))