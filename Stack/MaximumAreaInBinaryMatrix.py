from typing import List


def MaximumAreaOfHistogram(heights: list)->int:
    nsl_list = NSL(heights)
    nsr_list = NSR(heights)
    max_area = 0
    for i in range(len(heights)):
        area = (nsr_list[i]-nsl_list[i]-1)*heights[i]
        max_area = max(max_area,area)
    return max_area

def NSL(heights: list)->list:
    res = [] #will store index of nsl
    stack=[] #will store [nsl,index]
    for i in range(len(heights)):
        if(not len(stack)):
            res.append(-1)
            stack.append([heights[i],i])
            continue
        while(len(stack) and stack[-1][0]>=heights[i]):
            stack.pop()
        if(not len(stack)):
            res.append(-1)
        else:
            res.append(stack[-1][1])
        stack.append([heights[i],i])
    return res

def NSR(heights: list)->list:
    res = []
    stack=[]
    max_idx = len(heights)
    for i in range(len(heights)-1,-1,-1):
        if(not len(stack)):
            res.append(max_idx)
            stack.append([heights[i],i])
            continue
        while(len(stack) and stack[-1][0]>=heights[i]):
            stack.pop()
        if(not len(stack)):
            res.append(max_idx)
        else:
            res.append(stack[-1][1])
        stack.append([heights[i],i])
    res.reverse()
    return res

def MaximumAreaInBinaryMatrix(matrix: List[list])->int:
    matrix_height = len(matrix)
    running_1D_list = []
    max_area = 0
    for i in range(matrix_height):
        if(not len(running_1D_list)):
            running_1D_list = matrix[0]
            max_area = max(max_area,MaximumAreaOfHistogram(running_1D_list))
            continue
        running_1D_list = [(x+y if y>0 else 0) for x,y in zip(running_1D_list,matrix[i])]
        max_area = max(max_area,MaximumAreaOfHistogram(running_1D_list))
    return max_area

# Binary Matrix:
# [0,1,1,0,1]
# [1,1,1,1,1]
# [1,1,1,1,1]
# [1,1,0,0,1]

matrix = [[0,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,0,0,1]]

print(MaximumAreaInBinaryMatrix(matrix))