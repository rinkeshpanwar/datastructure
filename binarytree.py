class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data  = data


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

#printing the tree fully

