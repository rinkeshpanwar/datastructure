'''
@Code created by Prince Panwar. Happy coding. 
I'm programmer and I have no life.
'''
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlists:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        if self.head == None:
            self.head = node(data)
            self.tail = self.head
        else:
            self.tail.next = node(data)
            self.tail = self.tail.next

    def traverse(self):
        linkedlist = self.head
        if linkedlist == None:
            print("Linked list is empty")
            return
        while(linkedlist is not None):
            print(linkedlist.data,end=' ')
            linkedlist = linkedlist.next
    
    def deleteLastNode(self):
        ll = self.head
        if ll is None:
            return -1
        if self.head == self.tail:
            temp = self.head.data
            self.head = None
            self.tail = None
            return temp
        else:
            while(ll.next.next!= None):
                ll = ll.next
            deleted_node = ll.next.data
            self.tail = ll
            self.tail.next = None
            return deleted_node
    
    def addAtPosition(self,position,data):
        indexPosition = 0
        if self.head == None:
            return -1
        pointer = self.head
        while(pointer!= None):
            indexPosition+=1
            if indexPosition == position:
                temp = node(data)
                temp.next = pointer.next
                pointer.next = temp
                return data
            pointer = pointer.next
        print("no index found")
        return -1

    def deleteIndexNode(self,position):
        if self.head == None:
            return -1
        if position == 1:
            self.head = self.head.next
            return 1
        indexPosition = 0
        pointer = self.head
        while(pointer!=None):
            indexPosition+=1
            temp = pointer
            pointer = pointer.next
            if indexPosition == position:
                if pointer == self.tail:
                    self.tail = temp
                deleteValue = pointer.data
                temp.next = pointer.next
                return deleteValue
            
        print("No node is found")
        return -1
    def updateNodeData(self,data,newValue):
        pointer = self.head
        while pointer!=None:
            if pointer.data == data:
                pointer.data = newValue
                return pointer.data
            pointer = pointer.next
        print("Data has not been found")
        return -1

    def reverseLinkedList(self):
        if self.head == self.tail:
            print("There is only one node ")
            return -1
        pointer = self.head
        self.tail = self.head
        previous = None
        while(pointer!=None):   
            next = pointer.next
            pointer.next  = previous
            previous = pointer
            pointer = next
        self.head = previous
        return 1

   

check = 1
ll = linkedlists()
while(check!=0):
    print("-----------Menu for linked list-----------------")
    print("1.insert")
    print("2.Traverse")
    print("3.Delete Last Node")
    print("4.Insert value at specific index")
    print("5.Delete node at specific index")
    print("6.Update a node")
    print("7.Reverse a linked list")
    choice = int(input("Enter your choice"))
    if choice == 1:
        wantToInsert = 1
        while(wantToInsert!=0):
            insertValue = int(input("Enter value to insert:"))
            ll.insert(insertValue)
            wantToInsert = int(input("Do you want to continue 1->yes 0->no"))
    elif choice == 2:
        ll.traverse()
    elif choice == 3:
        deletedNode = ll.deleteLastNode()
        print("deleted node is {} in current list".format(deletedNode))
    elif choice == 4:
        data = int(input("Enter the value to be inserted"))
        indexPosition = int(input("Which index you want oto insert it"))
        print(ll.addAtPosition(indexPosition,data))
    elif choice == 5:
        position = int(input("Enter position at which you want to delete value"))
        deletedValue  = ll.deleteIndexNode(position)
        print("deleted value is ",deletedValue)
    elif choice == 6:
        indexValue = int(input("Enter which value you want to update : "))
        data = int(input("Enter the new updated value->"))
        returnValue = ll.updateNodeData(indexValue, data)
        print("Updated value is ->",returnValue)
    elif  choice == 7:
        status = ll.reverseLinkedList()
        print(status)
    else:
        break




