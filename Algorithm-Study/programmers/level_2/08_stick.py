def solution(arrangement):
    stack = []
    answer = 0
    i = 0
    while True :
        if arrangement[i] == '(' :
            if arrangement[i + 1] == ')' :
                answer += len (stack)
                i += 1
            else :
                stack.append('(')
        else :
            stack.pop()
            answer += 1
        i += 1
        if i == len (arrangement) :
            break
        
    
    return answer


arrangement = "()(((()())(())()))(())"
print(solution(arrangement))
