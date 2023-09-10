def find_NSR(arr: list) -> list:
    res = []
    stack = []
    for i in range(len(arr)-1,-1,-1):
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
    res.reverse()
    print("stack:",stack)
    return res

print(find_NSR([4,2,3,1]))