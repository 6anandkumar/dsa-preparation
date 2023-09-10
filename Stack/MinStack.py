class MinStack:
    stack = []
    ss = [] #Supporting Stack -> will always hold minimum element from stack
    def push(self,item: int):
        self.stack.append(item)
        if((not len(self.ss)) or (self.ss[-1] >= item)):
            self.ss.append(item)
    
    def pop(self):
        if((not len(self.stack)) or (not len(self.ss))):
            return "Stack Empty"
        el = self.stack.pop()
        if(el == self.ss[-1]):
            self.ss.pop()
        return el
    
    def getMinimum(self):
        if(not len(self.ss)):
            return "No items in stack"
        return self.ss[-1]

min_stack = MinStack()
min_stack.push(18)
min_stack.push(19)
min_stack.push(29)
min_stack.push(15)
min_stack.push(16)
print(min_stack.getMinimum())
min_stack.pop()
print(min_stack.getMinimum)
min_stack.pop()
print(min_stack.getMinimum())
min_stack.pop()
print(min_stack.getMinimum())
min_stack.pop()
print(min_stack.getMinimum())
min_stack.pop()
print(min_stack.getMinimum())
    
        