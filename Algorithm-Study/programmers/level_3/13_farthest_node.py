def solution(n, edges):
    graph = dict()
    distance = dict()

    for edge in edges:
        if min(edge) in graph:
            graph[min(edge)].append(max(edge))
            graph[min(edge)].sort()
        else:
            graph[min(edge)] = [max(edge)]

    distanceNum = 1
    nextList = graph[1]
    visited = [1]

    while len(visited) < n:
        temp = []
        for node in nextList:
            if node not in visited:
                visited.append(node)
                if distanceNum in distance:
                    distance[distanceNum] += 1
                else:
                    distance[distanceNum] = 1
                if node not in graph:
                    continue
                temp += graph[node]
        nextList = temp
        distanceNum = 2

    return distance[max(distance.keys())]
