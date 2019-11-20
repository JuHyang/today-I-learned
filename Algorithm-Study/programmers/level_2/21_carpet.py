def solution(brown, red):
    answer = []
    for i in range (1, red) :
        if red % i == 0 :
            if 2 * i + 2 * (red // i) + 4 == brown :
                answer.append (max (i + 2, red // i + 2)) 
                answer.append (min (i + 2, red // i + 2))
                break

    return answer