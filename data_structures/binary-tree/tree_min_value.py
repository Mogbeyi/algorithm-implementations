from collections import deque
from binary_tree import get_number_root

def get_min_value(root):
	queue = deque()
	queue.append(root)
	min_value = float('inf')

	while queue:
		current = queue.popleft()
		if current.value < min_value:
			min_value = current.value

		if current.left: queue.append(current.left)
		if current.right: queue.append(current.right)

	return min_value

def get_min_value(root):
	if not root:
		return float('inf')
	left = get_min_value(root.left)
	right = get_min_value(root.right)

	return min(root.value, left, right)




def main():
	root = get_number_root()
	print(get_min_value(root))

main()

