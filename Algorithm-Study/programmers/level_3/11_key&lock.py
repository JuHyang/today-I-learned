def rotate(key):
    M = len(key)
    result = []

    for i in range(M):
        temp = []
        for j in range(1, M + 1):
            temp.append(key[M - j][i])
        result.append(temp)
    return result


def check(rotated, lock):
    M = len(rotated)
    N = len(lock)
    for i in range(N + M - 1):
        for j in range(N + M - 1):
            board = list()
            for lo in lock:
                board.append(list(lo))

            offsetY = max(M - i - 1, 0)
            for k in range(max(0, i - M + 1), i + 1):
                offsetX = max(M - j - 1, 0)
                for l in range(max(0, j - M + 1), j + 1):
                    if k >= N or l >= N:
                        continue
                    board[k][l] += rotated[offsetY][offsetX]
                    if (board[k][l] != 1):
                        break
                    else:
                        board[k][l] = 1
                    offsetX += 1
                offsetY += 1
            status = True
            for o in range(N):
                for p in range(N):
                    if board[o][p] != 1:
                        status = False
                        break

            if status:
                return True
            else:
                continue

    return False


def solution(key, lock):
    rotated = key

    for i in range(4):
        result = check(rotated, lock)
        if (result == True):
            return True
        rotated = rotate(rotated)
    return False
