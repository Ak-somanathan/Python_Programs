class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"

        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"

        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()

s.push(2)
s.push(5)
print(s.pop())
s.push(7)
print(s.peek())
s.pop()
s.pop()
print(s.isEmpty())
    