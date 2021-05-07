def solution(board, moves):
    stack = []
    answer = 0
    
    for move in moves :
        index = move - 1
        for i in range (len (board)) :
            if board[i][index] == 0 :
                continue
            target = board[i][index]
            board[i][index] = 0
            if len (stack) == 0 :
                stack.append(target)
            else :
                if stack[-1] == target :
                    stack.pop()
                    answer += 2
                else :
                    stack.append(target)                    
            break
    return answer