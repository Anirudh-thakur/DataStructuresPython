#https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/

#Using list 

from queue import Queue
queue = []
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

# using deque (predefined in collection)
from collections import deque
print("Next Queue")
q = deque()
q.append('a')
q.append('b')
q.append('c')

print(q)
q.popleft()
print(q)

q.popleft()
q.popleft()
print(len(q) == 0)

# Using build in module Queue

from queue import Queue

#Max Size determines how many elements can a queue contain 
print("Next Queue")
qu = Queue(maxsize=3)
qu.put('A')
qu.put('B')
qu.put('C')
print(qu.full())
qu.get()


