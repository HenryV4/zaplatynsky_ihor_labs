def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def check_gas_delivery(cities_list, storages_list, pipe_list):
    graph = {city: [] for city in cities_list + storages_list}

    for pipe in pipe_list:
        source, destination = pipe
        graph[source].append(destination)

    visited = set()
    for storage in storages_list:
        dfs(graph, storage, visited)

    unreachable_cities = [city for city in cities_list if city not in visited]

    return unreachable_cities
