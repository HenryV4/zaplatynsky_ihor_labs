from collections import defaultdict

SOURCE = "Source"
FINAL = "Final"


def dfs(graph, vertex, final, visited, parent):
    """Depth-first search algorithm for traversing a graph

    Args:
        graph (dict): The graph represented as a dictionary
        vertex (object): The current vertex being visited
        final (object): The final vertex to reach
        visited (set): A set containing vertices that have been visited
        parent (dict): A dictionary containing the parent vertices for each vertex in the traversal

    Returns:
        bool: True if a path from the current vertex to the final vertex exists, False otherwise
    """
    if vertex == final:
        return True

    visited.add(vertex)

    for neighbor, capacity in graph[vertex].items():
        if capacity > 0 and neighbor not in visited:
            parent[neighbor] = vertex
            if dfs(graph, neighbor, final, visited, parent):
                return True

    return False


def ford_fulkerson(graph, source, final):
    """Ford-Fulkerson algorithm for finding the maximum flow

    Args:
        graph (dict): The graph represented as a dictionary
        source (object): The source vertex of the flow
        final (object): The final vertex of the flow

    Returns:
        int: The maximum flow from the source to the final vertex
    """

    max_flow = 0

    while True:
        parent = {}
        visited = set()
        if not dfs(graph, source, final, visited, parent):
            break

        path_flow = float("inf")
        vertex = final
        while vertex != source:
            parent_node = parent[vertex]
            path_flow = min(path_flow, graph[parent_node][vertex])
            vertex = parent_node

        vertex = final
        while vertex != source:
            parent_node = parent[vertex]
            graph[parent_node][vertex] -= path_flow
            vertex = parent_node

        max_flow += path_flow

    return max_flow


def read_file(filename):
    """Reads a data from a file

    Args:
        filename (str): The name of the file containing data

    Returns:
        tuple: A tuple containing lists of farms and stores, and a dictionary representing the graph
    """
    graph = defaultdict(dict)
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        farms = lines[0].strip().split(",")
        stores = lines[1].strip().split(",")
        for line in lines[2:]:
            start, destination, cars = line.strip().split(",")
            graph[start][destination] = int(cars)
    return farms, stores, graph


def write_output(max_cars, file_name):
    """Writes the maximum number of cars to a file

    Args:
        max_cars (int): The maximum number of cars
        file_name (str): The name of the output file
    """
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(max_cars))


def calculate_max_flow(filename):
    """Calculates the maximum flow for the given graph

    Args:
        filename (str): The name of the file containing the graph data

    Returns:
        int: The maximum flow in the graph
    """
    farms, stores, graph = read_file(filename)

    for farm in farms:
        graph[SOURCE][farm] = float("inf")
    for shop in stores:
        graph[shop][FINAL] = float("inf")

    max_flow = ford_fulkerson(graph, SOURCE, FINAL)
    return max_flow
