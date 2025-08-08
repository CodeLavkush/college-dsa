"""
Practical Details
sr no. 16
Date: 31 July 2025
"""

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

def main():
    my_heap = MaxHeap()
    while True:
        try:
            n = int(input("Enter number of elements: "))
            for _ in range(n):
                element = int(input("Enter a value: "))
                my_heap.insert(element)
                print(*my_heap.heap)
            break
        except Exception as error:
            print("ERROR:", error)

if __name__ == "__main__":
    main()