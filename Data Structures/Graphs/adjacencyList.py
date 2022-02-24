def add_node(graph_, new_node):
    if new_node in graph:
        print(f"Node {new_node} is already present in the given graph.")
    else:
        graph_[new_node] = []


def add_edge(graph_, node_from, node_to, weight=1, weighted=False, directed=False):
    if node_from not in graph_:
        print(f"Node {node_from} is not present in the Graph.")
    elif node_to not in graph_:
        print(f"Node {node_to} is not present in the Graph.")
    else:
        if not weighted:
            graph_[node_from].append(node_to)
            if not directed:
                graph_[node_to].append(node_from)
        else:
            graph_[node_from].append((node_to, weight))
            if not directed:
                graph_[node_to].append((node_from, weight))


def delete_node(n, graph_, weighted=False):
    if n not in graph_:
        raise ValueError("Node is not present in the given graph.")
    graph_.pop(n)
    if not weighted:
        for _, connections in graph_.items():
            if n in connections:
                connections.remove(n)
    else:
        for _, connections in graph_.items():
            for connection in connections:
                if connection[0] == n:
                    connections.remove(connection)


def delete_edge(node_from, node_to, graph_, directed=False):
    if node_from not in graph_:
        raise ValueError(f"Node {node_from} is not present in the Graph.")
    elif node_to not in graph_:
        raise ValueError(f"Node {node_to} is not present in the Graph.")
    else:
        graph_[node_from].remove(node_to)
        if not directed:
            graph_[node_to].remove(node_from)


def print_graph(graph_):
    for key, value in graph_.items():
        print(f"{key} -> {value}")


graph = {}
add_node(graph, 'A')
add_node(graph, 'B')
add_node(graph, 'C')
add_node(graph, 'D')
add_node(graph, 'E')
add_node(graph, 'F')
print_graph(graph)

add_edge(graph, 'A', 'C')
add_edge(graph, 'B', 'D')
add_edge(graph, 'E', 'C')
add_edge(graph, 'F', 'B')
add_edge(graph, 'A', 'D')

# add_edge(graph, 'A', 'C', 2, weighted=True, directed=True)
# add_edge(graph, 'B', 'D', 4, weighted=True, directed=True)
# add_edge(graph, 'E', 'C', 3, weighted=True, directed=True)
# add_edge(graph, 'F', 'B', 1, weighted=True, directed=True)
# add_edge(graph, 'A', 'D', 5, weighted=True, directed=True)

# add_edge(graph, 'A', 'C', 2, weighted=True)
# add_edge(graph, 'B', 'D', 4, weighted=True)
# add_edge(graph, 'E', 'C', 3, weighted=True)
# add_edge(graph, 'F', 'B', 1, weighted=True)
# add_edge(graph, 'A', 'D', 5, weighted=True)
print_graph(graph)
print()

delete_node('D', graph)
# delete_node('D', graph, weighted=True)
print_graph(graph)
print()

delete_edge('A', 'C', graph)
print_graph(graph)
