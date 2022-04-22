def add_node(existing_nodes, new_node):
    global node_count
    if new_node in existing_nodes:
        print(f"Node {new_node} is already present in the given graph.")
    else:
        node_count += 1
        existing_nodes.append(new_node)
        for row in graph:
            row.append(0)
        new_row = [0] * node_count
        graph.append(new_row)


def add_edge(node_from, node_to, existing_nodes, existing_graph, weight=1, directed=False):
    if node_from not in existing_nodes:
        print(f"Node {node_from} is not present in the Graph.")
    elif node_to not in existing_nodes:
        print(f"Node {node_to} is not present in the Graph.")
    else:
        index1 = existing_nodes.index(node_from)
        index2 = existing_nodes.index(node_to)
        existing_graph[index1][index2] = weight
        if not directed:
            existing_graph[index2][index1] = weight


def delete_node(n, nodes_, graph_):
    global node_count
    if n not in nodes_:
        raise ValueError("Node is not present in the given graph.")
    index = nodes_.index(n)
    nodes_.pop(index)
    node_count -= 1
    graph_.pop(index)
    for row in graph_:
        row.pop(index)


def delete_edge(node_from, node_to, nodes_, graph_, directed=False):
    if node_from not in nodes_:
        raise ValueError(f"Node {node_from} is not present in the Graph.")
    elif node_to not in nodes_:
        raise ValueError(f"Node {node_to} is not present in the Graph.")
    else:
        index1 = nodes_.index(node_from)
        index2 = nodes_.index(node_to)
        graph_[index1][index2] = 0
        if not directed:
            graph_[index2][index1] = 0


def print_graph(nodes_, graph_):
    print(' ', end=' ')
    for node in nodes:
        print(node, end=' ')
    print()
    # print('-' * 2 * (node_count + 2))
    for node, row in zip(nodes_, graph_):
        print(node, end=' ')
        for element in row:
            print(element, end=' ')
        print()


nodes = []
graph = []
node_count = 0
print("Before adding any nodes.")
print_graph(nodes, graph)

add_node(nodes, 'A')
print("After adding `A`.")
print_graph(nodes, graph)

add_node(nodes, 'B')
print("After adding `B`.")
print_graph(nodes, graph)

add_node(nodes, 'C')
print("After adding `C`.")
print_graph(nodes, graph)

add_node(nodes, 'D')
print("After adding `D`.")
print_graph(nodes, graph)

add_edge('A', 'C', nodes, graph, directed=True)
print("After connecting `A` and `C`.")
print_graph(nodes, graph)

add_edge('A', 'B', nodes, graph, 5, directed=True)
print("After connecting `A` and `C`.")
print_graph(nodes, graph)

add_edge('B', 'C', nodes, graph, 3, directed=True)
print("After connecting `B` and `C`.")
print_graph(nodes, graph)

delete_node('D', nodes, graph)
print("After deleting node `D`.")
print_graph(nodes, graph)

delete_edge('B', 'C', nodes, graph, directed=True)
print("After deleting edge between `B` and `C`.")
print_graph(nodes, graph)
