class tree():
    def __init__(self,val):
        self.value = val 
        self.left = None
        self.right = None


class t():
    def isIdentical(self,root1,root2):
        if root2==None:
            return True
        if root1 == None:
            return False
        if root1.value == root2.value:
            return self.check(root1,root2)
        return self.isIdentical(root1.left,root2) or self.isIdentical(root1.right, root2)
        
    def check(self,root1,root2):
        if root1==None and root2!=None:
            return False
        if root2==None:
            return True
        if root1.value==root2.value:
            return self.check(root1.left,root2.left) and self.check(root1.right,root2.right)
        return False

root = tree(10)
root.left = tree(20)
root.right = tree(30)
root.left.left = tree(40)
root.left.right = tree(50)
root.left.left.left = tree(60)

root2 = tree(20)
root2.left=tree(40)
root2.right = tree(50)
root2.left.left = tree(60)

t = t()
print(t.isIdentical(root,root2))