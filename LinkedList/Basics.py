#https://www.geeksforgeeks.org/linked-list-set-1-introduction/
class Node:
    #Function to initialise node object
    def __init__(self,data):
        # Assign data
        self.data = data;
        # Initialise next to None
        self.next = None;

class LinkedList:

    #Function to initialise head
    def __init__(self):
        self.head = None;

    #Function to print linked list 
    def printlist(self):
        temp = self.head;
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ =='__main__':
    llist = LinkedList();
    llist.head = Node(1);
    second = Node(2);
    third = Node(3);
    llist.head.next = second
    second.next = third
    llist.printlist()
