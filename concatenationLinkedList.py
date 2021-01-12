class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class concatenationLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head == None:
            temp = node(data)
            self.head = temp
            print("inserted at first node")
            return -1
        pointer = self.head
        while(pointer.next!=None):
            pointer = pointer.next
        temp = node(data)
        pointer.next = temp
        print("node added successfuly")
        return 1

    def concatenateList(self,obj):
        pointer = self.head
        while(pointer.next!=None):
            pointer = pointer.next
        pointer2 = obj.head
        while(pointer2!=None):
            pointer.next = pointer2
            pointer = pointer2
            pointer2 = pointer2.next
        print("concatenated usccessfully")
        return 1

    def traverseFirstList(self):
        if self.head == None:
            print("There is no node in list")
            return -1
        pointer = self.head
        while pointer!=None:
            print(pointer.data)
            pointer = pointer.next
        return 0
    def traverseTwoLinkedList(self,obj):
        if self.head == None:
            print("first linked list is empty")
            return -1
        pointer = self.head
        while(pointer!=None):
            print(pointer.data)
            pointer = pointer.next
        pointer2 = obj.head
        while pointer2!=None:
            print(pointer2.data)
            pointer2 = pointer2.next
        return 0


l1 = concatenationLinkedList()
l2 = concatenationLinkedList()
l2.insert(100)
l2.insert(200)
l2.insert(300)
l2.insert(400)

while True:
    print("-----------menu------------")
    print("1.insert")
    print("2.Traverse list")
    print("3.Traverse second list")
    print("4.concatenate list")
    menuChoice = int(input("Enter your choice->"))
    if menuChoice == 1:
        data = int(input("Enter your data->"))
        returnValue = l1.insert(data)
        print("Return value is->",returnValue)
    elif menuChoice == 2:
        returnValue = l1.traverseFirstList()
        print("Return value is->",returnValue)
    elif menuChoice == 3:
        returnValue = l1.traverseTwoLinkedList(l2)
        print("Return value is->",returnValue)
    elif menuChoice == 4:
        returnValue = l1.concatenateList(l2)
        print("Return value is->",returnValue)
    else:
        break