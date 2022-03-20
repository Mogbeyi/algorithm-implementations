class Node:

    def __init__(self, value):
        self.value = value
        self.next = None 

a = Node(2)
b = Node(3)
c = Node(8)
d = Node(7)

a.next = b
b.next = c
c.next = d

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


