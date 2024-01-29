# Accepted: 32ms (87.41%), 17.46MB (13.55%)

class MyQueue:
    def __init__(self):
        self.queue: Deque[int] = deque()

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def push(self, value: int) -> None:
        self.queue.append(value)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def size(self) -> int:
        return len(self.queue)

class MyStack:
    def __init__(self):
        self.queue = MyQueue()

    def push(self, x: int) -> None:
        self.queue.push(x)
        for _ in range(self.queue.size()-1):
            self.queue.push(self.queue.pop())

    def pop(self) -> int:
        if self.queue.size() == 0:
            raise Exception("stack underflow")

        return self.queue.pop()

    def top(self) -> int:
        if self.queue.size() == 0:
            raise Exception("stack underflow")

        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.isEmpty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
