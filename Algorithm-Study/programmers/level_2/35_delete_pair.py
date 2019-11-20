def solution(s):
    answer = 0
    list_char = []
    for i in range (len (s)) :
        if i == 0 :
            list_char.append(s[0])
        else :
            if len (list_char) != 0:
                if list_char[-1] == s[i] :
                    list_char.pop()
                else :
                    list_char.append(s[i])
            else :
                list_char.append(s[i])
    if len(list_char) == 0 :
        return 1
    else :
        return 0
