import pprint

edges = [
	['i', 'j'],
	['k', 'i'],
	['m', 'k'],
	['k', 'l'],
	['o', 'n']
]


def undirected_graph(edges, nodeA, nodeB, visited):
	graph = build_graph(edges)
	return has_path(graph, nodeA, nodeB, set())

def has_path(graph, src, dst, visited):
	if src == dst: return True
	if src in visited: return False
	visited.add(src)

	for neighbor in graph[src]:
		if has_path(graph, neighbor, dst, visited):
			return True

	return False


def build_graph(edges):
	graph = {}

	for edge in edges:
		a, b = edge

		if a not in graph: graph[a] = []
		if b not in graph: graph[b] = [] 
		graph[a].append(b)
		graph[b].append(a)

	return graph

# pprint.pprint(undirected_graph(edges, 'j', 'm'))
print(undirected_graph(edges, 'j', 'm', {}))

