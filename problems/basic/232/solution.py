# Accepted: 35ms (73.14%), 17.56MB (13.10%)

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

class MyQueue:
    def __init__(self):
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.size() == 0:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.size() == 0:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.size() == 0 and self.stack2.size() == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
