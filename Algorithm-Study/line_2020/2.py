def possible(orderNumber, ballNum):
    if orderNumber == ballNum[0]:
        return 0
    elif orderNumber == ballNum[-1]:
        return len(ballNum) - 1
    else:
        return -1


def solution(ball, order):
    answer = []

    subOrder = []

    orderIndex = 0
    while orderIndex < len(order):
        status = False
        for subNum in subOrder:
            ballIndex = possible(subNum, ball)
            if ballIndex != -1:
                answer.append(ball.pop(ballIndex))
                status = True
                break
        if status == True:
            continue

        ballIndex = possible(order[orderIndex], ball)

        if ballIndex == -1:
            subOrder.append(order[orderIndex])
        else:
            answer.append(ball.pop(ballIndex))

        orderIndex += 1

    return answer
