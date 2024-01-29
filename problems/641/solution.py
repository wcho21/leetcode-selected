# Accpeted: 59ms (92.10%), 18.09MB (19.15%)

class MyCircularDeque:
    def __init__(self, k: int):
        self.internalSize = k+1
        self.array = [0] * self.internalSize
        self.front = 0
        self.rear = 0

    def _getNextIndex(self, i: int) -> int:
        return (i+1) % self.internalSize

    def _getPrevIndex(self, i: int) -> int:
        return (i+self.internalSize-1) % self.internalSize

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.array[self.front] = value
        self.front = self._getNextIndex(self.front)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = self._getPrevIndex(self.rear)
        self.array[self.rear] = value
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = self._getPrevIndex(self.front)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = self._getNextIndex(self.rear)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        front = self._getPrevIndex(self.front)
        return self.array[front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.array[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self._getNextIndex(self.front) == self.rear


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
