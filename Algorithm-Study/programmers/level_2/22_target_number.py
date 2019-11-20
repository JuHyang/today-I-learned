def BFS (target, i, numbers, stack, result) :
    if i == len (numbers) - 1 :
        if stack + numbers[i] == target :
            result += 1
        if stack - numbers[i] == target :
            result += 1
        return result
    result = BFS (target, i + 1, numbers, stack + numbers[i], result)
    result = BFS (target, i + 1, numbers, stack - numbers[i], result)

    return result

def solution(numbers, target):

    answer = BFS (target, 0, numbers, 0, 0)

    return answer
