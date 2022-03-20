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

def get_index(head, idx):
    current = head

    for _ in range(idx):
        current = current.next

    return current.value

def get_index_recursive(head, idx):
    if not head:
        return None
    if not idx:
        return head.value
    return get_index_recursive(head.next, idx - 1)

print(get_index_recursive(a, 2))