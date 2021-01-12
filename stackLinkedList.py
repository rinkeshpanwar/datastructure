'''
linked list representation of stack created by rinkesh panwar
'''
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedListStack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head == None:
            self.head = node(data)
            return 1
        pointer = self.head
        self.head = node(data)
        self.head.next = pointer
        return 1

    def pop(self):
        if self.head == None:
            print("Stack is empty")
            return 0
        temp = self.head
        self.head = temp.next
        del(temp)
        print("deleted succesfully")
        return 1

    def peep(self):
        if self.head == None:
            print("Stack is empty")
            return 1
        pointer = self.head
        while(pointer!=None):
            print(pointer.data)
            pointer=pointer.next
        return 1

obj = linkedListStack()
while True:
    print("---------menu------------")
    print("1.Push")
    print("2.pop")
    print("3.peep")
    menuChoice = int(input("Enter your choice->"))
    if menuChoice == 1:
        data = input("Enter data to be inserted")
        returnValue = obj.push(data)
        print("Return value is->",returnValue)
    elif menuChoice == 2:
        returnValue = obj.pop()
        print("Return value is->",returnValue)
    elif menuChoice == 3:
        returnValue = obj.peep()
        print("Return value is->",returnValue)
    else:
        break