# Accepted: 62ms (79.34%), 17.97MB (20.49%)

class MyCircularQueue:
    def __init__(self, k: int):
        self.internalSize = k+1 # reserver extra one block to detect whether the queue is full
        self.array = [0] * self.internalSize
        self.toPush = 0
        self.toPop = 0

    def _getPrevIndex(self, index):
        return (index + self.internalSize-1) % self.internalSize

    def _getNextIndex(self, index):
        return (index+1) % self.internalSize

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.array[self.toPush] = value
        self.toPush = self._getNextIndex(self.toPush)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.toPop = self._getNextIndex(self.toPop)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.array[self.toPop]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        rear = self._getPrevIndex(self.toPush)
        return self.array[rear]

    def isEmpty(self) -> bool:
        return self.toPush == self.toPop

    def isFull(self) -> bool:
        return self._getNextIndex(self.toPush) == self.toPop

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
