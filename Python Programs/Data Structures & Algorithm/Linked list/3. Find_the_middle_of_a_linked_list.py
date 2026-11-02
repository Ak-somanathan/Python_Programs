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

    def findmiddle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow.data if slow else None


values = list(map(int, input().split()))

linked_list = LinkedList()

for i in values:
    linked_list.append(i)

print(linked_list.findmiddle())