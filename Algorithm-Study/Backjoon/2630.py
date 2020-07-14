def check (board, N, a, b) :
    result = [0, 0]
    first = board[a][b]
    if N == 1 :
        if first == '0' :
            return [1, 0]
        else :
            return [0, 1]

    status = True
    for i in range (a, a + N) :
        for j in range (b, b + N) :
            if i == a and j == b :
                continue
            if board[i][j] != first :
                status = False
                break
    if status == True :
        if first == '0' :
            return [1, 0]
        else :
            return [0, 1]
    else :
        resultTemp = check(board, N // 2 , a, b)
        (result[0], result[1]) = (result[0] + resultTemp[0], result[1] + resultTemp[1])
        resultTemp = check (board, N // 2, a + N // 2, b)
        (result[0], result[1]) = (result[0] + resultTemp[0], result[1] + resultTemp[1])
        resultTemp = check (board, N // 2, a, b + N // 2)
        (result[0], result[1]) = (result[0] + resultTemp[0], result[1] + resultTemp[1])
        resultTemp = check (board, N // 2, a + N // 2, b + N // 2)
        (result[0], result[1]) = (result[0] + resultTemp[0], result[1] + resultTemp[1])

    return result

N = int (input ())

board = []
for i in range (N) :
    listInput = input().split()
    board.append(listInput)

result = check (board, N, 0, 0)

print (result[0])
print (result[1])