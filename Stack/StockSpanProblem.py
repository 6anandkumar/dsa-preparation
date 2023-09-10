def stock_span(prices: list) -> list:
    res = []
    stack = []  #This will store [price,count_till_nearest_greater_to_left]
    for i in range(0,len(prices)):
        count = 1
        if(len(stack)==0):
            res.append(count)
            stack.append([prices[i],count])
            continue
        while(len(stack) and stack[-1][0]<=prices[i]):
            count+=stack[-1][1]
            stack.pop()
        res.append(count)
        stack.append([prices[i],count])
    return res

def stock_span2(prices: list) -> list:
    res = []
    stack = [] #This will store [price,index]
    for i in range(0,len(prices)):
        if(len(stack)==0):
            res.append(1)
            stack.append([prices[i],i])
            continue
        while(len(stack) and stack[-1][0]<=prices[i]):
            stack.pop()
        if(len(stack)==0):
            res.append(i)
        else:
            res.append(i-stack[-1][1])
        stack.append([prices[i],i])
    return res

print(stock_span([100,80,60,70,60,75,85]))
print(stock_span2([100,80,60,70,60,75,85]))