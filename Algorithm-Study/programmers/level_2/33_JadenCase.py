def solution(s):
    answer = ''
    for i in range (len (s)) :
        if i == 0 :
            answer += s[0].upper()
            continue

        if s[i] == " " :
            answer += " "
            continue
        
        if s[i - 1] == " " :
            answer += s[i].upper()
        else :
            answer += s[i].lower()
    return answer