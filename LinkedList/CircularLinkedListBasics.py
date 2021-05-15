class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        print(head.data)
        temp = temp.next
        while(temp != head):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    clist = CircularLinkedList()
    head = Node(1)
    N1 = Node(2)
    N2 = Node(3)
    clist.head = head
    head.next = N1
    N1.next = N2
    N2.next = head
    clist.printList()
