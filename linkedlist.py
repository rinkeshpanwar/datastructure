class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linkedList:

    def __init__(self):
        self.start_node = None
        self.end_node = None

    def insert(self,data):
        if self.start_node is None:
            self.start_node = node(data)
            self.end_node = self.start_node
        else:
            self.end_node.next = node(data)
            self.end_node = self.end_node.next
            
    def display(self):
        current = self.start_node
        while current is not None:
            print(current.data,end=' ')
            current = current.next

li = linkedList()
li.insert(10)
li.insert(15)
li.insert(20)
li.insert(10)
li.insert(15)
li.insert(20)
li.display()