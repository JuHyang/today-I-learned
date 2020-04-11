def combination(n, r):
    loopTime = int(min(r, n-r))
    result = 1
    for i in range(loopTime):
        result /= i + 1
        result *= n - i
    return int(result)


def solution(n, m, k):
    if n > m:
        return 0

    if k * n < m:
        return 0

    A = n / 2 + n % 2
    B = n - A

    answer = combination(m / 2 - 1, m / 2 - A) * \
        combination(m / 2 - 1, m / 2 - B) * 2

    tempA = 0
    tempB = 0

    if m / 2 - k - 1 > 0 and m / 2 - A - k > 0:
        tempA = combination(m / 2 - k - 1, m / 2 - A - k) * A

    if m / 2 - k - 1 > 0 and m / 2 - B - k > 0:
        tempB = combination(m / 2 - k - 1, m / 2 - A - k) * B

    answer = answer - (tempA * tempB * 2)

    if answer > 1000000007:
        answer = answer % 1000000007
    return answer
