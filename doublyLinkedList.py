class Node:
    def __init__(self,value=None):
        #three parts of node : prev|data|next
        self.prev=None
        self.data = value
        self.next=None
class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value) #temp Node obj created 
        if(self.head==None):    #if the linked list is empty.
            #self.head holds the address of leftmost Node (where prev is None)
            self.head = temp  #make self.head the first Node i.e. temp 
            return
        else:
            t=self.head  #t is a pointer node which now refers to first node
            while(t.next!=None):   #if next node is present, jump to it using t.next
                t=t.next
            #temp is the latest Node
            t.next=temp
            temp.prev=t

    def insertAtFront(self,value):
        temp=Node(value)
        if(self.head==None):    #if the linked list is empty.
            #self.head holds the address of leftmost Node (where prev is None)
            self.head = temp  #make self.head the first Node i.e. temp 
            return
        else:
            temp.next=self.head #temp.prev|temp.data|temp.next-->self.head-->DLL...
            self.head.prev = temp  #temp is now first node
            self.head=temp    #create diamgram to visualize and understamd

    def insertAtMiddle(self,value,x):
        t = self.head
        while(t.next!=None):   #if next node is present, jump to it using t.next
            if(t.data == x):
                break
            else:
                t=t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t
        #t<->temp<->t.next

    def delete(self,value):
        if(self.head==None):    
            print("Linked List is empty")
            return 
        else:
            t=self.head
            if(t.data ==value):
                self.head=t.next
                self.head.prev=None
                return
            
            while(t.next != None):
                if(t.data == value):
                    t.prev.next = t.next
                    t.next.prev = t.prev
                    return
                else:
                    t=t.next
            if(t.data ==value):
                t.prev.next = None                

    def printDoublyLL(self):
        t = self.head
        while(t.next!=None):
            print(t.data,end=" <-> ")
            t=t.next
        print(t.data)

obj = DoublyLL()
print("insertion at the end: ",end="")
obj.insertAtEnd(11)
obj.insertAtEnd(22)
obj.insertAtEnd(33)
obj.insertAtEnd(44)
obj.printDoublyLL()
print("insertion at the Begining: ",end="")
obj.insertAtFront(100)
obj.insertAtFront(200)
obj.printDoublyLL()
print("insertion in the middle: ",end="")
obj.insertAtMiddle(111,11)
obj.insertAtMiddle(222,22)
obj.printDoublyLL()
print("after deleting 33: ",end="")
obj.delete(33)
obj.printDoublyLL()
print("after deleting first element: ",end="")
obj.delete(200)
obj.printDoublyLL()
print("after deleting last element: ",end="")
obj.delete(44)
obj.printDoublyLL()


"""
FOR CIRCULAR DOUBLY LINKED LIST
1)lastnode.next != None
    lastnode.next == self.head  (it should point to the head node)
2)self.head.prev != None
    self.head.prev == lastNode  (it should point to the last node)
2)The condition in the while statement (t.next!=None) should be changed to (t.next!=self.head)
"""