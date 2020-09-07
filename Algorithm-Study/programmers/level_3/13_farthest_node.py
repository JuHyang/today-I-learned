def solution(n, edge):
    answer = 0

    graph = dict()
    distance = [0] * (n + 1)

    for numbers in edge:
        a = numbers[0]
        b = numbers[1]

        (a, b) = (min(a, b), max(a, b))

        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        graph[a].sort()

    print (graph)
    visited = set()
    visited.add(1)

    queue = [1]
    while len(queue) != 0:
        if len(visited) == n:
            break

        current = queue.pop(0)
        if current not in graph:
            continue

        for node in graph[current]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
                distance[node] = distance[current] + 1

    maxValue = max(distance)

    return distance.count(maxValue)
