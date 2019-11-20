def solution(answers):
    answer = []

    hum_1 = [1, 2, 3, 4, 5]
    hum_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    hum_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result_1 = 0
    result_2 = 0
    result_3 = 0

    index = 0
    for i in answers :
        if i == hum_1[index % 5] :
            result_1 += 1
        
        if i == hum_2[index % 8] : 
            result_2 += 1
        
        if i == hum_3[index % 10] :
            result_3 += 1

        index += 1


    if result_1 == max (result_1, result_2, result_3) :
        answer.append(1)

    if result_2 == max (result_1, result_2, result_3) :
        answer.append(2)

    if result_3 == max (result_1, result_2, result_3) :
        answer.append(3)

    return answer