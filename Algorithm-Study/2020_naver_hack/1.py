def solution(n, delivery):
    resultList = ['?'] * n

    sortedDelivery = sorted(
        delivery, key=lambda numbers: numbers[2], reverse=True)

    print(sortedDelivery)

    for i in range(len(sortedDelivery)):
        numbers = sortedDelivery[i]
        if numbers[2] == 1:
            resultList[numbers[0] - 1] = 'O'
            resultList[numbers[1] - 1] = 'O'
        else:
            if resultList[numbers[0] - 1] == 'O':
                resultList[numbers[1] - 1] = 'X'
            if resultList[numbers[1] - 1] == 'O':
                resultList[numbers[0] - 1] = 'X'

    answer = ''
    for result in resultList:
        answer += result

    return answer
