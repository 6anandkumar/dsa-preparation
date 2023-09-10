def find_NSL(arr: list) -> list:
    res = []
    stack = []
    for i in range(0,len(arr)):
        if len(stack)==0:
            res.append(-1)
            stack.append(arr[i])
            continue
        while(len(stack) and stack[-1]>=arr[i]):
            stack.pop()
        if len(stack)==0:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    print("stack:",stack)
    return res

print(find_NSL([1,2,3,4]))