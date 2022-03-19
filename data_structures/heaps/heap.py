import heapq

class MinHeap:
    def __init__(self, minheap):
        heapq.heapify(minheap)
        self.minheap = minheap

        def insert(self):
            heapq.heappush(self.minheap, key)

        def get_min(self):
            return self.minheap(0)

        def remove_min(self):
            heapq.heappop(self.minheap)

        def print_heap(self):
            print(self.minheap)


