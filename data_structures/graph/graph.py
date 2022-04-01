from collections import deque

graph = {
	'a': ['b', 'c'],
	'b': ['d'],
	'c': ['e'],
	'd': ['f'],
	'e': [],
	'f': []
}

def depth_first_print(graph, source):
	stack = deque()
	stack.append(source)

	while stack:
		current = stack.pop()
		print(current)

		for neighbour in graph[current]:
			stack.append(neighbour)

depth_first_print(graph, 'a')
