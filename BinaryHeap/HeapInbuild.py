from heapq import heapify,heappop,heappush

heap = []
heapify(heap)

heappush(heap,5)
heappush(heap, 3)
heappush(heap, 17)
heappush(heap,10)
heappush(heap,84)
heappush(heap, 19)
heappush(heap, 6)
heappush(heap, 22)
heappush(heap, 9)

print(heap)
heappop(heap)
print(heap)