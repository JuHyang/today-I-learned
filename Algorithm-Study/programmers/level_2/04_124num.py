def solution(n):
    answer = ""
    while True :
        status = 0
        if n % 3 == 1:
            answer = "1" + answer
        elif n % 3 == 2 :
            answer = "2" + answer
        elif n % 3 == 0 :
            answer = "4" + answer
            status = 1

        n = int(n / 3)
        if status == 1 :
            n -= 1
        if n == 0 :
            break
    return answer
