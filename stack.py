class Stack:
    def __init__(self):
        self.stk = []   #empty list 

    def length(self):
        return len(self.stk)
    
    def push(self,value):
        self.stk.insert(0,value)  #inserting element always at 0th index...
        # self.stk.append(value)  #can also use append 
        #insert will always add the element from the front and push the previous inserted elements backwards if any
        #append will always add the element in the end position 

    def peek(self):
        if (len(self.stk)==0):
            raise Exception("Stack is Empty")
        else:
            return f"Top most element: {self.stk[0]}"  #show latest element inserted 
        
    def pop(self):
        if (len(self.stk)==0):
            raise Exception("Stack is Empty")
        else:
            print("Element Removed: ",end="")
            return self.stk.pop(0)

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
print(stack1.peek())
print(stack1.pop())
print(stack1.peek())