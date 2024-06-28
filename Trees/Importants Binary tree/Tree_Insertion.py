#The tree can be binary but it is not necessary

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    #function to insert in the tree
    def insert(self,data):
        if self.data is None:
            self.data=data

        elif data<self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)

        elif data>self.data:
            if self.right is None:
                self.left=Node(data)
            else:
                self.right.insert(data)

root=Node("g")
root.insert("a")
root.insert("r")
root.insert("d")
root.insert("i")