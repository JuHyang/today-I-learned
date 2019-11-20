def solution(dartResult):
    listResult = []
    index = -1
    for i in dartResult :
        if i == "S" :
            listResult[index] = listResult[index] ** 1
        elif i == "D" :
            listResult[index] = listResult[index] ** 2
        elif i == "T" :
            listResult[index] = listResult[index] ** 3
        elif i == "#" :
            listResult[index] *= -1
        elif i == "*" :
            listResult[index] *= 2
            if index > 0 :
                listResult[index - 1] *= 2
        else :
            if i == "0" and index != - 1 and listResult[index] == 1:
                listResult[index] = 10
                continue
            listResult.append(int(i))
            index += 1
    answer = sum (listResult)
    return answer


dartResult = "1D2S#10S"
print (solution (dartResult))
