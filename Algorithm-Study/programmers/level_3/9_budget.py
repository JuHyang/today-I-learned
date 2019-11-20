def solution(budgets, M):
    if sum(budgets) <= M :
        return budgets[-1]
    
    answer = 0
    budgets.sort()
    answer = M // len (budgets)
    
    count = 0
    result = M
    for i in range (len (budgets)) :
        if budgets[i] <= answer :
            result -= budgets[i]
            count = i
        else :
            break
    while True :
        temp = budgets[count + 1:]
        if answer * (len (temp)) > result :
            return answer - 1
        else :
            answer += 1
            for i in range (len (temp)) :
                if temp[i] > answer :
                    break
                else :
                    count += 1
                    result -= temp[i]