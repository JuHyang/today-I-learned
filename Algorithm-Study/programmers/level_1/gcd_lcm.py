def solution(n, m):
    answer = []
    a = -1
    b = -1
    
    if m > n :
        a, b = m, n
    else :
        a, b = n, m

    while b != 0 :
        temp = b
        b = a % b
        a = temp
        if b > a :
            a, b = b, a
    answer.append(a)
    result = n * m // a
    answer.append(result)
    return answer