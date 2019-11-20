def solution(clothes):
    answer = 1
    temp = dict()
    for cloth in clothes :
        if cloth[1] in temp :
            temp[cloth[1]].append(cloth[0])
        else :
            temp[cloth[1]] = [cloth[0]]

    for i in temp :
        answer *= (len (temp[i]) + 1)
    
    return answer - 1