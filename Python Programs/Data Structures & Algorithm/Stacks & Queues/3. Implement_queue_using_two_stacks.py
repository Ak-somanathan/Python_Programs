class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue underflow"

        return self.stack2.pop()

q = queue()

n = int(input())

for _ in range(n):
    operation = input().split()

    if operation[0] == 'enq':
        q.enqueue(int(operation[1]))

    elif operation[0] == 'deq':
        print(q.dequeue())
