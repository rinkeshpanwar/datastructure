class node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        if self.head == None:
            self.head = node(data)
            self.tail = self.head
            return self.head.data
        temp = node(data)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        return temp.data

    def showVlaue(self):
        if self.head == None:
            return -1

        if self.head == self.tail:
            print(self.head.data)
            return 0
        pointer = self.head
        while(pointer!=None):
            print(pointer.data)
            pointer = pointer.next
        return 0
#print the given linked list 
#if linkedList is a->b->c->d->e
#change its value to a->e->b->d->c
    def facebookInterview(self):
        if self.head is None:
            return -1
        start = self.head
        end = self.tail
        while(start!=end and start!=end.next):
            print(start.data)
            start  = start.next
            print(end.data)
            end = end.prev
        if start == end:
            print(start.data)
        return 0


fll = doubleLinkedList()
while True:
    print("---------------MENU----------------")
    print("1.insert")
    print("2.Show value")
    print("3.Facebook Interview Solution")
    menuChoice = int(input("Enter your chouice->"))
    if menuChoice == 1:
        noOfData = int(input("How many element you want in list"))
        i=0
        while(i<noOfData):
            data = input("Enter number")
            fll.insert(data)
            i+=1
    elif menuChoice == 2:
        returnValue = fll.showVlaue()
        print("return value is ->",returnValue)
    elif menuChoice == 3:
        returnValue = fll.facebookInterview()
        print("return value is->",returnValue)
    else:
        break
