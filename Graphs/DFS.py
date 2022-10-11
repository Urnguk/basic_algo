def DFS(adjacency_list, visited_set=None, current_node=0):
    if visited_set is None:
        visited_set = set()
    visited_set.add(current_node)
    for next_node in adjacency_list[current_node]:
        if next_node not in visited_set:
            DFS(adjacency_list, visited_set, next_node)
    return visited_set


V, E = (int(x) for x in input().split())
graph = [[] for x in range(V)]
for i in range(E):
    start, finish = (int(x) for x in input().split())
    graph[start].append(finish)
    graph[finish].append(start)
connectivity_component = DFS(graph)
print(*connectivity_component)
