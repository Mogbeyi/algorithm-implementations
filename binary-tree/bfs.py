class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#a = Node('a')
#b = Node('b')
#c = Node('c')
#d = Node('d')
#e = Node('e')
#f = Node('f')
#
#a.left = b
#a.right = c
#b.left = d
#b.right = e
#c.right = f
#
a = Node(3)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(-2)
f = Node(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#
#def breadth_first_search(root):
#    queue = [root]
#    total = 0
#
#    while queue:
#        curr = queue.pop(0)
#        total += curr.value
#
#        if (curr.left != None):
#            queue.append(curr.left)
#        if (curr.right != None):
#            queue.append(curr.right)
#
#    return total 

def minNumberOfOperations(k):
    queue = [1]
    seen_values = set()
    min_num_of_operations = 0

    while queue:
        result = queue.pop(0)
        if result == k:
            return min_num_of_operations
        elif result == 0:
            continue
        elif result in seen_values: 
            continue
        else:
            min_num_of_operations += 1
            queue.append(result * 2)
            queue.append(result // 3)
        seen_values.add(result)

    return min_num_of_operations

print(minNumberOfOperations(10))

