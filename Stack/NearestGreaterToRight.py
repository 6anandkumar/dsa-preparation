def find_NGR(arr: list) -> list:
    res = []
    stack = []
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            res.append(-1)
            stack.append(arr[i])
            continue
        while(len(stack) and stack[-1]<=arr[i]):
            stack.pop()
        if len(stack)==0:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    res.reverse()
    print("stack:",stack)
    return res

print(find_NGR([1,3,2,4]))