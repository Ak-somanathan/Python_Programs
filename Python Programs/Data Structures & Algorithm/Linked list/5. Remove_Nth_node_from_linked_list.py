class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self. tail = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

def removeNthNode(head, n):
    dummy = Node(0)
    dummy.next = head

    slow = fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next

def display(head):
    while head:
        print(head.data, end = "")
        if head.next:
            print("->", end="")
        head = head.next
    
values = list(map(int, input().split()))
n = int(input())

linked_list = LinkedList()

for i in values:
    linked_list.append(i)

removed = removeNthNode(linked_list.head, n)

display(removed)