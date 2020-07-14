p = 1000000007


def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (a * power(a, b - 1)) % p
    else:
        half = power(a, b // 2) % p
        return half * half % p


listInput = input().split()

N = int(listInput[0])
K = int(listInput[1])

if N == 1 or N == K or K == 0 or N == 0:
    print(1)
else:
    factorial = [1, 1]

    for i in range(2, N + 1):
        factorial.append(factorial[-1] * i % p)

    a = factorial[N]
    b = (factorial[K] * factorial[N - K]) % p

    b2 = power(b, p - 2)
    result = (a * b2) % p

    print(result)
