class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#a = Node(3)
#b = Node(2)
#c = Node(7)
#d = Node(4)
#e = Node(-2)
#f = Node(5)
#
#a.left = b
#a.right = c
#b.left = d
#b.right = e
#c.right = f
#
def depth_first_search(root):
    if not root:
        return
    print(root.value)
    depth_first_search(root.left)
    depth_first_search(root.right)

depth_first_search(a)


