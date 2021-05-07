def solution(s):
    answer = []
    s = s[1:-1]
    sList = s.split("}")
    i = 0
    while i < len(sList) :
        if sList[i] == "" :
            sList.pop(i)
            continue
        
        if i == 0 :
            sList[i] = sList[i][1:].split(",")
        else :
            sList[i] = sList[i][2:].split(",")
        
        i += 1
    sList.sort(key=len)
    
    for ss in sList :
        for num in ss :
            if int(num) in answer :
                continue
            else :
                answer.append(int(num))

    return answer