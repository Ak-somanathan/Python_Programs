class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

def mergeList(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next 

        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next

def display(head):
    while head:
        print(head.data, end = "")
        if head.next:
            print("->", end = "")
        head = head.next


values1 = list(map(int, input().split()))
values2 = list(map(int, input().split()))

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

for i in values1:
    linked_list_1.append(i)

for i in values2:
    linked_list_2.append(i)

merged_list = mergeList(linked_list_1.head, linked_list_2.head)

display(merged_list)