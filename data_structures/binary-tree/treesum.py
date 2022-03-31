from collections import deque
from binary_tree import get_number_root

def tree_sum_recursive(root):
	if not root:
		return 0
	return tree_sum_recursive(root.left) + root.value + tree_sum_recursive(root.right)

def tree_sum_iterative(root):
	queue = deque()
	queue.append(root)
	total = 0

	while queue:
		current = queue.popleft()

		if current.left: queue.append(current.left)
		if current.right: queue.append(current.right)
		total += current.value

	return total

def main():
	root = get_number_root()
	print(tree_sum_iterative(root))

main()

