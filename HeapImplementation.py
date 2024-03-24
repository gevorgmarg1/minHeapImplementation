class MinHeap:
    def __init__(self, capacity):
        self.heap = [0] * capacity
        self.capacity = capacity
        self.size = 0
    def getParentIndex(self, index):
        return (index-1)//2
    def getLeftChildIndex(self, index):
        return index*2 + 1
    def getRightChildIndex(self, index):
        return index*2 + 2
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    def parent(self, index):
        return self.heap[self.getParentIndex(index)]
    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]
    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]
    def isFull(self):
        return self.size == self.capacity
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    def insert(self, value):
        if(self.isFull()):
            print("Heap is full")
            return 0
        self.heap[self.size] = value
        self.size += 1
        self.heapifyUp()
    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            if self.heap[index] > self.heap[smallerChildIndex]:
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex
            else:
                break   
    def removeMin(self):
        if(self.size == 0):
            print("Heap is empty!")
            return 0
        min = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heapifyDown()
        self.heap[self.size-1] = 0
        self.size -= 1
        return min

heap1 = MinHeap(3)
heap1.insert(3)
heap1.insert(20)
heap1.insert(5)
heap1.removeMin()
print(heap1.heap)