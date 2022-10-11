def BFS(adjacency_list, start_node=0, visited_set=None):
    if visited_set is None:
        visited_set = {start_node}
    LIFO = [start_node]
    while LIFO:
        current_node = LIFO.pop()
        for next_node in adjacency_list[current_node]:
            if next_node not in visited_set:
                visited_set.add(next_node)
                LIFO.append(next_node)
    return visited_set


V, E = (int(x) for x in input().split())
graph = [[] for x in range(V)]
for i in range(E):
    start, finish = (int(x) for x in input().split())
    graph[start].append(finish)
    graph[finish].append(start)
connectivity_component = BFS(graph)
print(*connectivity_component)
