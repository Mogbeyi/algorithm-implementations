class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

def print_linked_list(head):
    values = []
    current = head

    while current:
        values.append(current.value)
        current = current.next

    return '->'.join(values)

def print_linked_list_recursive(head):
    if head == None:
        return 
    print(head.value)
    return print_linked_list_recursive(head.next)

# print(print_linked_list(a))

print_linked_list_recursive(a)

