def solution(words, queries):
    answer = [0] * len (queries)

    for i in range(len (queries)) :
        for word in words :
            if len (queries[i]) != len (word) :
                continue

            status = True
            if queries[i][0] == '?' :
                for j in range (1, len (queries[i]) + 1) :
                    if queries[i][-j] == '?' :
                        break
                    if queries[i][-j] != word[-j] :
                        status = False
                        break
            else :
                for j in range (len (queries[i])) :
                    if queries[i][j] == '?' :
                        break
                    if queries[i][j] != word[j] :
                        status = False
                        break
            if status :
                    answer[i] += 1
    
    return answer