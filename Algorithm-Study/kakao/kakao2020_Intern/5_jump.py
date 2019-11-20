def solution(stones, k):
    answer = 0

    nextIndex = dict ()
    for i in range (len (stones)) :
        nextIndex[i] = i + 1
    status = True
    while status :
        for key, value in nextIndex.items() :
            if value - key > k :
                status = False
                break

        if status == False :
            break
        
        for i in range (len (stones)) :
            if stones[i] == 0 :
                continue
            stones[i] = max (0, stones[i] - 1)
            if stones[i] == 0 :
                temp = nextIndex[i]
                del nextIndex[i]
                before = i - 1
                nextIndex[before] = temp

                before = max (-1, before - 1)
                while stones[before] == 0 :
                    if before in nextIndex :
                        nextIndex[before] = temp
                    if before == 0 :
                        break
                    before = max (0, before - 1)
        answer += 1


    return answer




# def solution(stones, k):
#     answer = 0

#     status = True
#     while status :
#         temp = []
#         for i in range (len (stones)) :
#             if stones[i] != 0 :
#                 temp.append(stones[i])
#             if stones[i] == 0 and i <= len (stones) - k:
#                 for j in range (i, i + k) :
#                     if stones[j] != 0 :
#                         break

#                     if j == i + k - 1 :
#                         status = False

#         if status == False :
#             break
#         minValue = min (temp)
#         for i in range (len (stones)) :
#             stones[i] = max (0, stones[i] - minValue)
#         answer += minValue


#     return answer


