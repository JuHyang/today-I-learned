import sys

read = sys.stdin.readline

N = int(read())

if N == 1:
    print(1)
else:
    num = 2
    while num < N:
        num *= 2

    if num == N:
        print(N)
    else:
        print(2 * (N - num // 2))
