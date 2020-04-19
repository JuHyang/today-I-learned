def solution(operations):

    queue = []

    for operation in operations:
        inputList = operation.split()

        if inputList[0] == 'I':
            if len(queue) == 0:
                queue.append(int(inputList[1]))
            else:
                if int(inputList[1]) < queue[-1]:
                    queue.append(int(inputList[1]))
                for i in range(len(queue)):
                    if queue[i] < int(inputList[1]):
                        queue.insert(i, int(inputList[1]))
                        break
        else:
            if len(queue) == 0:
                continue

            if int(inputList[1]) == 1:
                queue.pop(0)
            else:
                queue.pop(-1)

    if len(queue) == 0:
        return [0, 0]
    else:
        return [queue[0], queue[-1]]
