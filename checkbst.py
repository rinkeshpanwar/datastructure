class node():
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

class tree():
    def __init__(self):
        self.arr = []
    def insert(self,val):
        return node(val)

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        self.arr.append(root.value)
        self.inorder(root.right)
t = tree()
root = t.insert(50)
root.left = t.insert(40)
root.right = t.insert(70)
root.left.left = t.insert(25)
root.left.right = t.insert(45)

t.inorder(root)
if sorted(t.arr) == t.arr:
    print("this is binary search tree")
else:
    print("They are not bst")