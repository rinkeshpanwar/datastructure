class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class queueLinkedList:
    def __init__(self):
        self.rear = None
    
    def insert(self,data):
        if self.rear == None:
            self.rear = node(data)
            self.rear.next = self.rear
            print("Inserted first elemet")
            return 1
        temp = node(data)
        temp.next = self.rear.next
        self.rear.next = temp
        self.rear = temp
        print("Elemenet added succesfully")
        return 1
    
    def display(self):
        if self.rear == None:
            print("queu is empty")
            return 1
        pointer = self.rear.next
        while True:
            print(pointer.data)
            pointer = pointer.next
            if pointer == self.rear.next:
                break
        return 1
    
    def delete(self):
        if self.rear == None:
            print("queue is empty")
            return 0
        pointer = self.rear.next
        self.rear.next = pointer.next
        return pointer.data

obj = queueLinkedList()
while True:
    print("--------------Menu----------")
    print("1.Insert")
    print("2.Delete")
    print("3.Display")
    menuChoice = int(input("Enter your choice"))
    if menuChoice == 1:
        data = int(input("Enter your data to be inserted"))
        returnValue = obj.insert(data)
        print("Return value is ",returnValue)
    elif menuChoice == 2:
        returnValue = obj.delete()
        print("Return value is ",returnValue)
    elif menuChoice == 3:
        returnValue = obj.display()
        print("Return value is ",returnValue)
    else:
        break