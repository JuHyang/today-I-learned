def DFS (V, list_graph, list_mark, result) : ## 깊이우선 탐색
    if list_mark[V - 1] == True :
        return
    result.append(V)
    list_mark[V - 1] = True
    for i in list_graph[V - 1] :
        DFS (i, list_graph, list_mark, result)

    return result

def BFS (V, list_graph, list_mark, list_inQueue) :
    result = []
    queue = [V]
    list_inQueue[V - 1] = True

    while len (queue) != 0:
        current = queue.pop(0)
        result.append(current)
        list_mark[current - 1] = True
        for i in list_graph[current - 1] :
            # print (list_mark)
            # print (list_inQueue)
            if list_mark[i - 1] == False and list_inQueue[i - 1] == False :
                # print (queue)
                queue.append(i)
                list_inQueue[i - 1] = True

    return result

def inputGraph (N, M) :
    list_result = []
    for i in range (0, N) :
        list_temp = []
        list_result.append(list_temp)

    for i in range (0, M) :
        input_str = input ()
        list_input = input_str.split()
        list_result[int(list_input[0]) - 1].append(int(list_input[1]))

    return list_result

def printResult (result) :
    result_str = ""
    for i in result :
        result_str += str(i) + " "

    print (result_str)
def main () :
    input_str = input ()
    list_input = input_str.split()
    N = int (list_input[0])
    M = int (list_input[1])
    V = int (list_input[2])

    list_mark = []
    for i in range (N) :
        list_mark.append(False)

    list_graph = inputGraph (N, M)
    # print (list_graph)

    printResult (DFS (V, list_graph.copy(), list_mark.copy(), []))

    printResult (BFS (V, list_graph.copy(), list_mark.copy(), list_mark.copy()))

main()
