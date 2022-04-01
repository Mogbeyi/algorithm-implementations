from collections import deque

graph = {
	'a': ['b', 'c'],
	'b': ['d'],
	'c': ['e'],
	'd': ['f'],
	'e': [],
	'f': []
}

# def has_path(graph, src, dest):
# 	if src == dest:
# 		return True

# 	for neighbour in graph[src]:
# 		exist = has_path(graph, neighbour, dest)
# 		if exist:
# 			return True

# 	return False

def has_path(graph, src, dest):
	queue = deque()
	queue.append(src)

	while queue:
		current = queue.popleft()
		if current == dest:
			return True

		for neighbour in graph[current]:
			queue.append(neighbour)

	return False


print(has_path(graph, 'a', 'e'))
