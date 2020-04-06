def solution(budgets, M):
    budgets.sort()
    if sum(budgets) <= M:
        return budgets[-1]

    
    money = 0
    standard = 0
    index = 0
    for i in range(len(budgets)):
        if (money + budgets[i] * (len(budgets) - i) > M):
            index = i
            standard = budgets[i]
            break
        else:
            money += budgets[i]

    temp = M - money

    return temp // (len (budgets) - index)
