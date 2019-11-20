def solution(n, words):
    answer = [0, 0]

    list_words = []
    list_words.append(words[0])

    status = True
    turn = 0
    for i in range (1, len (words)) :
        turn += 1
        turn %= n

        if  list_words[-1][-1] != words[i][0] :
            status = False
        elif words[i] in list_words :
            status = False
        else :
            list_words.append(words[i])

        if status == False :
            answer[0] = turn + 1
            answer[1] = i // n + 1 
            break
    return answer