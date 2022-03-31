from collections import deque
from binary_tree import get_root

# def depth_first_values(root):
# 	stack = deque()
# 	stack.append(root)
# 	result = []

# 	while stack:
# 		node = stack.pop()
# 		result.append(node.value)

# 		if node.right:
# 			stack.append(node.right)
# 		if node.left:
# 			stack.append(node.left)


# 	return '->'.join(result)

def depth_first_values(root):
	if not root:
		return []

	left = depth_first_values(root.left)
	right = depth_first_values(root.right)

	return [root.value, *left, *right]

def main():
	root = get_root()
	result = depth_first_values(root)

	print(result)

main()

