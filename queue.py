class Queue:
    def __init__(self):
        self.queue = []    #empty list 

#queue full --> overflow
#queue empty --> underflow

    def isEmpty(self):
        print ("Queue is empty" if (len(self.queue) == 0) else "Queue is not empty")
    
    def insert(self,value):
        self.queue.append(value)    #insertion from back

    def delete(self): 
        if(len(self.queue)==0): 
            print("Underflow Condition")
        else:
            print(self.queue.pop(0))   #deletion from front
        
    def peek(self):
        print(self.queue[0])


q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.isEmpty()
q.peek()
q.delete()
q.delete()
q.delete()
q.delete()
q.isEmpty()