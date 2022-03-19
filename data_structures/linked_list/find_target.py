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

def find_target(head, target):
    current = head

    while current:
        if current.value == target:
            return True
        current = current.next

    return False


def find_target_recursive(head, target):
    if not head:
        return False
    if head.value == target:
        return True
    return find_target_recursive(head.next, target)


print(find_target_recursive(a, 7))
print(find_target_recursive(a, 17))



