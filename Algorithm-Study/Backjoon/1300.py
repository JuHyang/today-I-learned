N = int(input())
K = int(input())

count = 1
index = 1
while K > index:
    K -= index

    if index < N:
        index += 1
    else:
        index -= 1

    count += 1

if K == 0:
    K = count

if count > N:
    gap = N - count
    K += gap
    count -= gap


print(K * (count - K))
