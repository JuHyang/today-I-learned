def solution(s):
    answer = ""
    mode = True
    for char in s :
        if char == " " :
            answer += char
            mode = True
            continue
            
        if mode :
            answer += char.upper()
            mode = False
        else :
            answer += char.lower()
            mode = True
    return answer