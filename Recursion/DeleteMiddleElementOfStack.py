import math
def deleteMid(stack):
    if(not len(stack)):
        return stack
    mid = math.floor(len(stack)/2)+1
    delete(stack,len(stack)-mid)
    return stack

def delete(stack,n):
    if(n==0 and len(stack)):
        stack.pop()
        return
    top = stack.pop()
    delete(stack,n-1)
    stack.append(top)
    return

print(deleteMid([1,2,3,4,5]))
    