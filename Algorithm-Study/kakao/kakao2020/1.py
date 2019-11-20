def implicit (s, n) :
    index = n
    before = s[:index]
    count = 1
    result = ""
    aim = ''

    while True :
        index += n
        if index > len (s) + 1 :
            if count == 1 :
                result += before
            else :
                result += str(count) + before
            result += s[index-n:]
            break
        aim = s[index - n:index]
        if before == aim :
            count += 1 
        else :
            if count == 1 :
                result += before
            else :
                result += str(count) + before
            before = aim
            count = 1

    return len (result)

def solution(s):
    answer = len (s)
    for i in range (1, len(s) + 1) :
        result = implicit (s, i)
        if answer > result :
            answer = result
    return answer