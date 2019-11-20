def solution(strings, n):
    answer = []
    answer.append(strings[0])

    for i in strings[1:] :
        index = 0
        while True :
            if answer[index][n] > i[n] :
                answer.insert(index, i)
                break
            elif answer[index][n] == i[n] :
                if answer[index] > i :
                    answer.insert(index, i)
                    break

            index += 1
            if index == len (answer) :
                answer.append(i)
                break

    return answer