from collections import deque
from binary_tree import get_root

# def includes(root, target):
# 	queue = deque()
# 	queue.append(root)

# 	while queue:
# 		current = queue.popleft()

# 		if current.value == target:
# 			return True

# 		if current.left: queue.append(current.left)
# 		if current.right: queue.append(current.right)

# 	return False

def includes(root, target):
	if not root: return False 
	if root.value == target: return True

	return includes(root.left, target) or includes(root.right, target)


def main():
	root = get_root()
	result = includes(root, 'c')

	print("Value exist") if result else print("Value does not exist")

main()

