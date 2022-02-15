from collections import deque

def bfs(name, graph):
    queue = deque()
    queue += graph[name]
    searched = []

    while queue:
        person = queue.popleft()
        
        if person not in searched:
            if person_is_seller(person):
                print("Person is mango seller")
                return True
            else:
                queue += graph[person]
                searched.append(person)

    return False


