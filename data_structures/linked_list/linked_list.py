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

def linked_list_values(head):
    values = []
    fill_values(head, values)
    return values

def fill_values(head, values):
    if head == None:
        return
    values.append(head.value)
    return fill_values(head.next, values)

print(linked_list_values(a))
