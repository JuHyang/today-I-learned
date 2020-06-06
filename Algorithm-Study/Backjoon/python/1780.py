def paper (board, y, x, size) :
    result = [0, 0, 0]

    start = board[y][x]

    if size == 1 :
        if start == "-1" :
            result[0] += 1
        elif start == "0" :
            result[1] += 1
        elif start == "1" :
            result[2] += 1

        return result

    status = True

    for i in range (y, y + size) :
        for j in range (x, x + size) :
            if start != board[i][j] :
                status = False
                break
        
        if status == False :
            break

    if status == True :
        if start == "-1" :
            result[0] += 1
        elif start == "0" :
            result[1] += 1
        elif start == "1" :
            result[2] += 1
    else :
        nextSize = size // 3
        temp = paper (board, y, x, nextSize) 
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y + nextSize, x, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y + nextSize * 2, x, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y, x + nextSize, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y + nextSize, x + nextSize, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y + nextSize * 2, x + nextSize, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y, x + nextSize * 2, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y + nextSize, x + nextSize * 2, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
        temp = paper (board, y + nextSize * 2, x + nextSize * 2, nextSize)
        (result[0], result[1], result[2]) = (result[0] + temp[0], result[1] + temp[1], result[2] + temp[2])
    
    return result
    


N = int (input ())

board = []

for i in range (N) :
    board.append(input().split())

for board in paper(board, 0, 0, N) :
    print (board)