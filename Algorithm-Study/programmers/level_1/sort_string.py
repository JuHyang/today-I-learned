def isUpper (c) :
    if c == c.upper() :
        return True
    else :
        return False

def solution(s):
    answer = ''
    list_lower = []
    list_upper = []
    for c in s:
        if isUpper(c) :
            if len (list_upper) == 0 :
                list_upper.append(c)
                continue
            for i in range (len(list_upper)) :
                if list_upper[i] < c :
                    list_upper.insert(i, c)
                    break
                if i == len(list_upper) - 1 :
                    list_upper.append(c)
        else :
            if len (list_lower) == 0 :
                list_lower.append(c)
                continue
            for i in range (len(list_lower)) :
                if list_lower[i] < c :
                    list_lower.insert(i, c)
                    break
                if i == len(list_lower) - 1 :
                    list_lower.append(c)

    for i in list_lower :
        answer += i
    for i in list_upper :
        answer += i
    return answer