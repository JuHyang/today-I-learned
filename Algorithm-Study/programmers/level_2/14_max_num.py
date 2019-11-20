def solution(number, k):
    answer = ''

    o = len(number) - k
    for i in range (1, o + 1) :
        temp = number[:len(number) - o + i]
        max_letter = "0"
        max_letter_index = 0
        for j in range (len(temp)) :
            if temp[j] == '9' :
                max_letter = '9'
                max_letter_index = j
                break
            if temp[j] > max_letter :
                max_letter = temp[j]
                max_letter_index = j
        number = number[max_letter_index + 1:]
        answer += max_letter
        if len(answer) + len (number) == o :
            answer += number
            break
    
    return answer