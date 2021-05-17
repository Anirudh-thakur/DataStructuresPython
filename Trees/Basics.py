#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def printInorder(self):
        if self.data :
            if self.left != None:
                self.left.printInorder()
            print(self.data)
            if self.right != None:
                self.right.printInorder()
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def search(self,val):
        if self.data:
            if self.data == val:
                print("Value Found")
            elif val < self.data:
                if self.left == None:
                    print("Value Not Found")
                else:
                    self.left.search(val)
            else:
                if self.right == None:
                    print("Value Not Found")
                else:
                    self.right.search(val)
        else:
            print("Value not found")
                

if __name__ == '__main__':
    root = Node(3)
    root.insert(1)
    root.insert(4)
    root.insert(-1)
    root.insert(7)
    root.printInorder()
    root.search(-1)
