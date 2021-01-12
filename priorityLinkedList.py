class node:
    def __init__(self,priority,data):
        self.priority = priority
        self.data = data
        self.next = None

class priorityQueue:
    def __init__(self):
        self.front = None
    
    def insert(self,priority,data):
        if self.front == None:
            self.front = node(priority,data)
            print("Node added in front of queue")
            return 1
        if priority < self.front.priority:
            temp = node(priority,data)
            temp.next = self.front
            self.front = temp
            return 1
        pointer = self.front.next
        previous = self.front
        while(pointer!=None):
            if priority < pointer.priority:
                temp = node(priority,data)
                temp.next = pointer
                previous.next = temp
                return 1
            previous = pointer
            pointer = pointer.next
        temp = node(priority,data)
        previous.next = temp
        print("Added at last node")
        return 1

    def display(self):
        if self.front == None:
            print("queue is empty")
            return 1
        pointer = self.front
        while(pointer!=None):
            print("priority->",pointer.priority," data->",pointer.data)
            pointer = pointer.next
        return 1

pq = priorityQueue()
pq.insert(1,10)
pq.insert(2,20)
pq.insert(3,30)
pq.insert(4,40)
pq.insert(2,50)
pq.insert(1,60)
pq.insert(3,70)
pq.insert(-3,70 0)
pq.display()
        

