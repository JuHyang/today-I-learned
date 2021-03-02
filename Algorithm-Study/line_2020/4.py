def getValue(position, maze):
    return maze[position[0]][position[1]]


def solution(maze):
    answer = 0

    direction = 0
    if maze[0][1] == 0:
        direction = 3
    elif maze[1][0] == 0:
        direction = 2

    current = [0, 0]
    print(current, direction)
    while True:
        if direction == 0:
            current[0] -= 1
        elif direction == 1:
            current[1] -= 1
        elif direction == 2:
            current[0] += 1
        elif direction == 3:
            current[1] += 1
        answer += 1

        if current[0] == current[1] == len(maze) - 1:
            break

        nextDirection = (direction + 1) % 4
        while True:
            nextPosition = current.copy()

            if nextDirection == 0:
                nextPosition[0] -= 1
            elif nextDirection == 1:
                nextPosition[1] -= 1
            elif nextDirection == 2:
                nextPosition[0] += 1
            elif nextDirection == 3:
                nextPosition[1] += 1

            if len(maze) not in nextPosition and -1 not in nextPosition and getValue(nextPosition, maze) != 1:
                direction = nextDirection
                break
            nextDirection -= 1
            if nextDirection < 0:
                nextDirection += 4

    return answer


solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]])
