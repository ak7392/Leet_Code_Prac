graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {
    'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def dijkstra_fun(graph, start, goal):

    predecessor = {}
    shortest_path = {}
    infinity = 999999
    unseen_nodes = graph
    path = []

    for node in unseen_nodes:
        shortest_path[node] = infinity
    shortest_path[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_path[node] < shortest_path[min_node]:
                min_node = node

        for childNode, weight in graph[min_node].items():
            if weight + shortest_path[min_node] < shortest_path[childNode]:
                shortest_path[childNode] = weight + shortest_path[min_node]
                predecessor[childNode] = min_node
        unseen_nodes.pop(min_node)

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except:
            print("Path is unreachable")
    path.insert(0, start)
    if shortest_path[goal] != infinity:
        print("Shortest distance" + ": "+str(shortest_path[goal]))
        print("Shortest path" + str(path))


dijkstra_fun(graph, 'a', 'e')
