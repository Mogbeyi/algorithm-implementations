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

def sum_linked_list(head):
    total = 0
    current = head

    while current:
        total += current.value
        current = current.next

    return total

def recursive_sum_linked_list(head):
    if not head:
        return 0
    return head.value + recursive_sum_linked_list(head.next)

# print(sum_linked_list(a))
print(recursive_sum_linked_list(a))

