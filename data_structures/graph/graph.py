from collections import deque

graph = {
	'a': ['b', 'c'],
	'b': ['d'],
	'c': ['e'],
	'd': ['f'],
	'e': [],
	'f': []
}

# def depth_first_print(graph, source):
# 	stack = deque()
# 	stack.append(source)

# 	while stack:
# 		current = stack.pop()
# 		print(current)

# 		for neighbour in graph[current]:
# 			stack.append(neighbour)


def depth_first_print(graph, source):
	print(source)

	for neighbour in graph[source]:
		depth_first_print(graph, neighbour)

def breath_first_print(graph, source):
	queue = deque()
	queue.append(source)

	while queue:
		current = queue.popleft()
		print(current)

		for neighbour in graph[current]:
			queue.append(neighbour)

# depth_first_print(graph, 'a')
breath_first_print(graph, 'a')
