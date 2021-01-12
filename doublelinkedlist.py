class node:
    def __init__(self,data):
        self.previous = None
        self.data = data
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.start = None

    def insert(self,data):
        pointer = self.start
        if self.start == None:
            self.start = node(data)
            return self.start.data
        while(pointer.next!=None):
            pointer = pointer.next
        temp = node(data)
        pointer.next = temp
        temp.previous = pointer
        return temp.data
    
    def traverse(self):
        if self.start == None:
            print("List is empty")
            return -1
        pointer = self.start
        while(pointer!=None):
            print(pointer.data)
            pointer = pointer.next
        return 1

    def insertBeforeData(self, data,inputData):
        if self.start.data == data:
            temp = node(inputData)
            temp.next = self.start
            self.start.previous = temp
            self.start = temp
            return self.start.data
        pointer = self.start
        while(pointer!=None):
                if pointer.data == data:
                    temp = node(inputData)
                    temp.next = pointer
                    temp.previous = pointer.previous
                    previousPointer = pointer.previous
                    previousPointer.next = temp
                    return temp.data
                pointer = pointer.next
        print("No matching value found")
        return -1
    def deleteDataNode(self,data):
        if self.start.data == data:
            self.start = self.start.next
        previous = self.start
        pointer = self.start.next
        while(pointer!=None):
            if pointer.data == data:
                previous.next = pointer.next
                pointer = pointer.next
                pointer.previous = previous
                return 1
            pointer = pointer.next
        print("No data found with that data")
        return 0

    def reverseLinkedList(self):
        if self.start == None:
            print("Linked List is empty")
            return -1
        
        pointer = self.start
        temp = None
        while(pointer is not None):
            temp = pointer.previous
            pointer.previous = pointer.next
            pointer.next = temp
            pointer = pointer.previous
        
        self.start = temp.previous
        '''p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.previous = p2
        while(p2!=None):
            p2.previous = p2.next
            p2.next = p1
            p1=p2
            p2=p2.previous

        self.start = p1'''
        return 0
        '''
        [previous, data, next]->[previous,data,next]->[previous,data,next]
        '''

dll = doubleLinkedList()
choice = 0
while(True):
    print("---------------menu for Double linked list---------------")
    print("1.Insertion in Linked list")
    print("2.Traverse through Linked list")
    print("3.Insert data before node")
    print("4.delete data node")
    print("5.Reverse a doubly linked list")
    menuInput = int(input("Enter your choice->"))
    if menuInput == 1:
        InsertionData = int(input("Enter value to be inserted->"))
        returnValue = dll.insert(InsertionData)
        print("Returned value is:",returnValue)
    elif menuInput == 2:
        returnValue = dll.traverse()
        print("Return value is:",returnValue)
    elif menuInput == 3:
        data = int(input("Enter your data to be inserted"))
        beforeData = int(input("Enter before which data to be inserted"))
        returnValue = dll.insertBeforeData(beforeData,data)
        print("return value is ->",returnValue)
    elif menuInput == 4:
        data = int(input("Enter your data to be deleted"))
        returnValue = dll.deleteDataNode(data)
        print("Return value is->",returnValue)
    elif menuInput == 5:
        returnValue = dll.reverseLinkedList()
        print("return value is",returnValue)
    else:
        break
