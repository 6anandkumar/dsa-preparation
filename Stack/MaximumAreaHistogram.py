def index_of_nsl(heights: list) -> list:
    res = []    
    stack = []  
    for i in range(0,len(heights)):
        if(len(stack)==0):
            res.append(-1)
            stack.append([heights[i],i])
            continue
        while(len(stack) and stack[-1][0]>=heights[i]):
            stack.pop()
        if(len(stack)):
            res.append(stack[-1][1])
        else:
            res.append(-1)
        stack.append([heights[i],i])
    
    return res

def index_of_nsr(heights: list) -> list:
    res = []
    stack = []
    for i in range(len(heights)-1,-1,-1):
        if(len(stack)==0):
            res.append(len(heights))
            stack.append([heights[i],i])
            continue
        while(len(stack) and stack[-1][0]>=heights[i]):
            stack.pop()
        if(len(stack)):
            res.append(stack[-1][1])
        else:
            res.append(len(heights))
        stack.append([heights[i],i])
    res.reverse()
    return res

def maximum_area_under_histogram(heights: list)->int:
    nsl = index_of_nsl(heights)
    nsr = index_of_nsr(heights)
    print("nsl:",nsl)
    print("nsr:",nsr)
    max_area = 0
    areas=[]
    for i in range(len(heights)):
        area = (nsr[i]-nsl[i]-1)*heights[i]
        max_area = max(max_area,area)
        areas.append(area)
    print("areas:",areas)
    return max_area

print(maximum_area_under_histogram([6,2,5,4,5,1,6]))
            