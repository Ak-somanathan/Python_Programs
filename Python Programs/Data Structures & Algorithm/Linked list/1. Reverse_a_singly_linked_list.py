# node initializing class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# head and tail initialization
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        self.tail = None if self.head is None else self.head

        while self.tail and self.tail.next:
            self.tail = self.tail.next


values = list(map(int, input().split()))

linked_list = LinkedList()

for i in values:
    linked_list.append(i)

linked_list.display()

linked_list.reverse()

linked_list.display()