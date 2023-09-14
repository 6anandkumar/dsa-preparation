#Stack can simply be reversed using another stack, but here it is done using recursion using SC-O(1)

def reverseStack(stack):
    if(len(stack)==0 or len(stack)==1):
        return stack
    return reverse(stack)

def reverse(stack):
    if(len(stack)==0):
        return
    top = stack.pop()
    reverseStack(stack)
    insert_at_bottom(stack,top)
    return stack
def insert_at_bottom(stack,item):
    if(not len(stack)):
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack,item)
    stack.append(top)
    return

print(reverseStack([1,2,3,4,5]))