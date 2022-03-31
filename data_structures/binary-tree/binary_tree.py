class Node:

	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

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

g = Node(3)
h = Node(11)
i = Node(4)
j = Node(4)
k = Node(2)
l = Node(3)

g.left = h
g.right = i
h.left = j
h.right = k
i.right = l

def get_root():
	return a

def get_number_root():
    return g
