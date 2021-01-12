class stackList:
    def __init__(self):
        self.stack = [0,0,0,0,0]
        self.top = -1
        self.max = 5
    def push(self,data):
        if self.top == self.max-1:
            print("Stack is full")
            return 0
        self.top+=1
        self.stack[self.top]=data
        print("inserted successfully")
        return 1
    def pop(self):
        if(self.top == -1):
            print("Stakc is empty")
            return 0
        self.top-=1
        return 0
    def peep(self):
        if(self.top == -1):
            print("Stack is empty")
            return 1
        for i in range(self.top+1):
            print(self.stack[i])
        return 0
    def noOfElement(self):
        if(self.top == -1):
            print("Stack is empty")
            return 0
        return self.top+1

obj = stackList()
while True:
    print("---------menu------------")
    print("1.Push")
    print("2.pop")
    print("3.peep")
    print("4.No of element")
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
    elif menuChoice == 4:
        returnValue = obj.noOfElement()
        print("Return value is->",returnValue)
    else:
        break
