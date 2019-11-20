def solution(n):
    answer = []
    answer.append (0)

    for i in range (n - 1) :
        temp = []
        for j in range (len (answer)) :
            if answer[j] == 0 :
                temp.append(1)
            else :
                temp.append(0)
        temp.reverse()
        answer += [0] + temp

    return answer
