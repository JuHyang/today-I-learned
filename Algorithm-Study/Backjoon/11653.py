N = int(input())
target = 2
while N != 1:
    if N % target == 0:
        print(target)
        N = N // target
        continue

    target += 1
