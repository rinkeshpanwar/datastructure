'''
Don't implement circular queue use only fixed size index queue
simple queue using list
'''

class queue:
    def __init__(self):
        self.q = [0,0,0,0,0]
        self.front = -1
        self.rear = -1
    def isFull(self):
        if self.rear == 4 or self.front == 4:
            return 1
        else:
            return 0
    def isEmpty(self):
        if (self.front and self.rear == -1) or (self.front > self.rear):
            return 1
        else:
            return 0
    def insert(self,data):
        if self.isFull():
            print("Queu is full")
            return 0
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.q[self.rear] = data
            print("element is added in first place")
            return 1
        self.rear+=1
        self.q[self.rear] = data
        print("data inserted succesfully")
        return 1
    def delete(self):
        if self.isEmpty():
            print("queue is empty")
            return 0
        self.front+=1
        print("queue is deleted succesfully")
        return 0
    def display(self):
        if self.isEmpty():
            print("queue is empty")
            return 0
        for i in range(self.front,self.rear+1):
            print(self.q[i])
        return 1

obj = queue()
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
