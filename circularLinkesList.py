class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        if self.head == None:
            temp  = node(data)
            temp.next = temp
            self.head = temp
            self.tail = self.head
            print("First node is added")
            return 0
        temp = node(data)
        self.tail.next = temp
        temp.next = self.head
        self.tail = temp
        print("added next node")
        return 0

    
    def traverse(self):
        if self.head == None:
            print("Circular linked list is empty")
            return 0
        pointer = self.head
        while True:
            print(pointer.data)
            pointer = pointer.next
            if pointer == self.head:
                return 0
            
        return 0 

    def deleteDataNode(self,data):
        if self.head == None:
            print("Linked list is empty")
            return 0
        if self.head.data == data:
            self.head = self.head.next
            self.tail.next = self.head
            print("Deleted Data at first Node")
            return 0
        pointer = self.head
        while(pointer!=None):
            if pointer.next.data == data:
                if pointer.next == self.tail:
                    pointer.next = self.tail.next
                    self.tail = pointer
                    print("Tail has been changed")
                    return 0
                temp = pointer.next
                pointer.next = temp.next
                del(temp)
                print("Data is deleted from linked list")
                return 0
            pointer = pointer.next
        print("Data is not found in linked list")
        return -1


cll = circularLinkedList()
while True:
    print("1.insert in circular linked list")
    print("2.Traverse in a circular linked list")
    print("3.Delete data from linked list")
    menuChoice = int(input("Eneter your choice->"))
    if menuChoice == 1:
        data = int(input("Enter data to be inserted"))
        returnValue = cll.insert(data)
        print("Return Value is->",returnValue)

    elif menuChoice == 2:
        returnValue = cll.traverse()
        print("return value is->",returnValue)
    elif menuChoice == 3:
        data = int(input("Enter data to be deleted"))
        returnValue = cll.deleteDataNode(data)
        print("return value is->",returnValue)
    else:
        break