def solution(board):
    answer = 0
    dp = []
    row = len (board)
    col = len (board[0])
    for i in range (row) :
        temp = []
        for j in range (col) :
            if i == 0 or j == 0:
                value = board[i][j]
                if answer < value :
                    answer = value
                temp.append (value)
                continue
                
            if temp[-1] != 0 and dp[i - 1][j] != 0 and dp[i - 1][j - 1] != 0 and board[i][j] != 0 :
                value = min (temp[-1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                temp.append(value)
            else :
                value = board[i][j]
                temp.append(value)
            if answer < value :
                    answer = value
        dp.append(temp)
    answer = answer ** 2
    return answer
