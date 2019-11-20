def pushList (x, y, board) :
    for i in range (x) :
        board[x - i][y] = board[x- i - 1][y]
    
    board[0][y] = ""

def downBoard (m, n, board) :
    for j in range (n) :
        for i in range (m) :
            if board[i][j] == "":
                pushList(i, j, board)

def checkBoard (m, n, board) :
    while True :
        delete = []
        for i in range(m - 1) :
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != "":
                    delete.append([i, j])
                    delete.append([i, j + 1])
                    delete.append([i + 1, j])
                    delete.append([i + 1, j + 1])
        if len (delete) == 0 :
            break
        for i in delete :
            board[i[0]][i[1]] = ""

        downBoard(m, n, board)
    return board

def solution(m, n, board):
    boardNew = []
    for i in range (m) :
        temp = []
        for j in range (n) :
            temp.append(board[i][j])
        boardNew.append(temp)
    boardNew = checkBoard(m, n, boardNew)
    
    answer = 0
    for i in boardNew :
        answer += i.count("")
    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print (solution (m, n, board))
