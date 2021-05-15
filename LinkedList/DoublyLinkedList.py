class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def printNode(self):
        node = self.head
        print("List in normal order ")
        while node != None:
            print(node.data,  end=" "),
            last = node
            node = node.next
        print("\nList in reverse order")
        while(last != None):
            print(last.data,  end=" "),
            last = last.prev
        
if __name__ == '__main__':
    N1 = Node(1)
    N2 = Node(2)
    N3 = Node(3)
    N4 = Node(4)
    DList = DoublyLinkedList()
    DList.head = N1
    N1.next = N2
    N2.prev = N1
    N2.next = N3
    N3.prev = N2
    N3.next = N4
    N4.prev = N3
    DList.printNode()

