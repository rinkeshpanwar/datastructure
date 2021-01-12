import collections
class node:
    def __init__(self,data=None):
        self.data = data
        self.left =None
        self.right = None

class tree:
    def __init__(self):
        self.dq = collections.deque()
    def insert(self,data):
        return node(data)
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
    def inverse(self,root):
        if root == None:
            return
        self.inverse(root.left)
        self.inverse(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    def bst(self,root):
        if root==None:
            self.dq.append(root)
            return
        print(root.data)
        self.dq.append(root.left)
        self.dq.append(root.right)
        self.bst(self.dq.popleft())




t = tree()
root = t.insert(10)
root.left = t.insert(20)
root.right = t.insert(30)
root.left.left = t.insert(40)
root.left.right = t.insert(50)
root.right.left = t.insert(60)
root.right.right = t.insert(70)
root.right.right.right = t.insert(70)
#t.inorder(root)
#t.inverse(root)
print("---------------------")
#t.inorder(root)
t.bst(root)