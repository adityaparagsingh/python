class DeQueue:  #doubly ended Queue
    def __init__(self):
        self.dequeue = []    #empty list 

#dequeue full --> overflow
#dequeue empty --> underflow

    def isEmpty(self):
        print ("Queue is empty" if (len(self.dequeue) == 0) else "Queue is not empty")
    
    def insertAtEnd(self,value):
        self.dequeue.append(value)    #insertion from back

    def deleteAtFront(self): 
        if(len(self.dequeue)==0): 
            print("Underflow Condition")
        else:
            print(self.dequeue.pop(0))   #deletion from front
        
    def insertAtFront(self,value):
        self.dequeue.insert(0,value)
    
    def deleteAtEnd(self):
        print(self.dequeue.pop())
    
    def peekEnd(self):
        print(self.dequeue[-1])
    def peekFront(self):
        print(self.dequeue[0])


q = DeQueue()
q.insertAtEnd(10)
q.insertAtFront(20)
q.insertAtEnd(30)
q.isEmpty()
q.peekEnd()
q.peekFront()
q.deleteAtEnd()
q.deleteAtFront()
q.deleteAtFront()
q.isEmpty()