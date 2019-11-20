def solution(board):
    answer = 0
    result = []
    for i in range (len (board)) :
        temp = []
        for j in range (len (board[0])) :
            if i == 0 or j == 0 :
                temp.append(board[i][j])
            else :
                if board[i][j] == 0 :
                    temp.append(0)
                else :
                    if result[i - 1][j - 1] != 0 and temp[j - 1] != 0 and result[i - 1][j] != 0 :
                        temp.append(min (result[i - 1][j - 1], temp[j - 1], result[i - 1][j]) + 1)
                    else :
                        temp.append(board[i][j])
            if temp[-1] > answer :
                answer = temp[-1]
        result.append(temp)

    answer = answer ** 2

    return answer