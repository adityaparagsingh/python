class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self,head = None):
        self.head = head     #head points to the first node
                            # If list is empty → head = None

    def insertAtEnd(self,value):
        temp = Node(value)  #temp is an temporary object of Node class
        if(self.head!=None):
            t1 = self.head  #t1 starts at head
            while(t1.next!=None):   #t1 reaches the end node using loop
                t1 = t1.next #head..nextnode...nextnode....lastNode(temp)
            t1.next = temp  #Last node’s next is updated to temp
        else:
            self.head = temp
    
    def insertAtFront(self,value):
        temp = Node(value)  #temp node created using value
        temp.next = self.head    # The new node’s next now points to the current head
        self.head = temp   #New node becomes the first node...Head now points to the new node

    def insertAtMiddle(self,value,x):  #x is data from LL
        temp = Node(value)
        t1 = self.head
        while(t1!= None):
            if(t1.data==x):
                temp.next = t1.next #new node ka next will point to x ke baad wala node (x(t1)-->temp-->t1.next(temp.next))
                t1.next = temp     #new t1.next is x ka next node which will hold temp(new Node to be inserted)
            t1 = t1.next      #traversing 
            #temp is new node to be added
            #t1 is a old node 

    def deleteLL(self,y):
        t1 = self.head
        prev = t1
        if(t1.data==y):     #for head Node,
            self.head=t1.next   #t1.data = y then point to next node(t1.next)
        while(t1.next!=None):
            if(t1.data==y):
                prev.next=t1.next   #if y found ...prev.next will skip t1(delete/ignore it) and points to next mode to t1
                return
            else:
                prev = t1    #if y not found...prev(head) becomes t1(current)
                t1 = t1.next   #t1(head) is now t1.next (next node to head)..again loop contiues
        if(t1.data==y):      #for last node,
            prev.next=None   #will store None in the second last or prev node to t1 instead of t1 address

    def printLL(self):
        t1=self.head   #t1 starts at head
        while(t1.next != None):
            print(t1.data,end="->")
            t1 = t1.next
        print(t1.data)

obj = SinglyLinkedList()
print("inserting at the end: ",end="")
obj.insertAtEnd(11)
obj.insertAtEnd(22)
obj.insertAtEnd(33)
obj.insertAtEnd(44)
obj.printLL()
print("inserting at the beginning: ",end="")
obj.insertAtFront(100)
obj.insertAtFront(200)
obj.printLL()
print("inserting in the middle: ",end="")
obj.insertAtMiddle(6,33)   #insert 6 after 33
obj.insertAtMiddle(7,6)    #insert 7 after 6
obj.printLL()
obj.deleteLL(100)
print("After deleting:",end="")
obj.printLL()

"""
FOR CIRCULAR SINGLY LINKED LIST
1)lastnode.next != None
    lastnode.next == self.head  (it should point to the head node)
2)The condition in the while statement (t.next!=None) should be changed to (t.next!=self.head)
"""