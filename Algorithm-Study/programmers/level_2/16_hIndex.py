def solution(citations):
    temp = sorted (citations)
    if temp[-1] == 0 :
        return 0
    for i in range (len (temp)) :
        if temp[i] >= len (temp) - i :
            return len(temp) - i