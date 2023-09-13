def sortStack(st):
    stack = st[:]
    if(0<=len(stack)<=1):
        return stack
    old_top = stack.pop()
    sorted_stack = sortStack(stack)
    helper_stack = []
    while(len(sorted_stack) and sorted_stack[-1]>old_top): #if '>' then top will be biggest, if '<' then top will be smallest
        helper_stack.append(sorted_stack.pop())
    sorted_stack.append(old_top)
    while(len(helper_stack)):
        sorted_stack.append(helper_stack.pop())
    return sorted_stack

print(sortStack([5,4,2,6,0,4,2,4,1]))