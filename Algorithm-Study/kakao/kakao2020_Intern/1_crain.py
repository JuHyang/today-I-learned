def solution(board, moves):
    answer = 0

    stack = []
    
    for move in moves :
        move = move - 1
        for i in range (len (board)) :
            if board[i][move] != 0 :
                if len (stack) == 0 :
                    stack.append(board[i][move])
                    board[i][move] = 0
                    break

                if board[i][move] == stack[-1] :
                    stack.pop()
                    board[i][move] = 0
                    answer += 2
                    break
                else :
                    stack.append(board[i][move])
                    board[i][move] = 0
                    break
    return answer