#https://www.geeksforgeeks.org/binary-heap/
#https://www.geeksforgeeks.org/min-heap-in-python/
# Min heap

import sys
class Heap:
    def __init__(self,max):
        self.max = max
        self.size = 0
        self.heap = [0] * max
        self.heap[0] = -1 * sys.maxsize
        self.top = 1
    def resize(self):
        self.heap = self.heap + [0] * max
        self.max = self.max * 2
    def parent(self,pos):
        return pos//2
    def leftChild(self,pos):
        return pos*2 
    def rightChild(self,pos):
        return pos*2 + 1
    def swap(self,pos1 , pos2):
        self.heap[pos1] , self.heap[pos2] = self.heap[pos2] , self.heap[pos1]
    def isLeafNode(self,pos):
        if pos>= (self.size //2) and pos <= self.size:
            return True
        return False
    def minHeapify(self,pos):
        if not self.isLeafNode(pos):
            if (self.heap[pos] > self.heap[self.rightChild(pos)]) or (self.heap[pos] > self.heap[self.leftChild(pos)]):
                if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]:
                    self.swap(self.leftChild(pos),pos)
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(self.rightChild(pos),pos)
                    self.minHeapify(self.rightChild(pos))
    def insert(self,val):
        if self.size >= self.max:
            self.resize()
        self.size = self.size + 1
        self.heap[self.size] = val
        current = self.size
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))
            current = self.parent(current)

    def minHeap(self):
        for i in range(self.size//2, 0,-1):
            self.minHeapify(i)
    
    def print(self):
        for i in range(1,(self.size // 2) +1):
            p_String = " PARENT : " + str(self.heap[i])+" LEFT CHILD : " +str(self.heap[2 * i])
            if 2 * i + 1 <= self.size:
                p_String = p_String + " RIGHT CHILD : " +str(self.heap[2 * i + 1])
            print(p_String)
    def remove(self):
        removed = self.heap[self.top]
        self.heap[self.top] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size-=1
        self.minHeapify(self.top)
        return removed


if __name__ == "__main__":

    print('The minHeap is ')
    minHeap = Heap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    minHeap.print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.print()

