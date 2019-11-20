def solution(n):
    answer = 0

    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    m = int (n ** 0.5)
    for i in range (2, m + 1) :
        if prime[i] :
            for j in range (i + i, n + 1, i) :
                prime[j] = False
    answer = prime.count(True)
    return answer

