from collections import deque
from binary_tree import get_root

def breadth_first_search(root):
	if not root: return []

	queue = deque()
	queue.append(root)
	result = []

	while queue:
		current = queue.popleft()
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)

		result.append(current.value)

	return '->'.join(result)

def main():
	root = get_root()
	result = breadth_first_search(root)

	print(result)



main()
