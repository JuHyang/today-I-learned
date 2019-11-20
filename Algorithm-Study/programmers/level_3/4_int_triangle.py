def solution(triangle):
    answer = 0
    list_answer = []
    for i in range (len (triangle)) :
        temp = []
        for j in range (len (triangle[i])) :
            if i == 0 :
                temp.append(triangle[i][0])
                break

            value = 0
            if j == 0 :
                value = triangle[i][j] + list_answer[i - 1][0]
            elif j == len (triangle[i]) - 1 :
                value = triangle[i][j] + list_answer[i - 1][j - 1]
            else :
                value = triangle[i][j] + max (list_answer[i - 1][j], list_answer[i - 1][j - 1])
            temp.append(value)
        list_answer.append(temp)
    answer = max (list_answer[-1])
    return answer