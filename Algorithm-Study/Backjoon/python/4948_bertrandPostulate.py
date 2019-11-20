list_prime = [2]

for i in range (3, 246913) :
    for j in list_prime :
        if j ** 2 > i :
            list_prime.append(i)
            break
        if i % j == 0 :
            break

while True :
    n = int (input ())

    if n == 0 :
        break

    count = 0

    for i in list_prime :
        if n < i <= 2 * n :
            count += 1
        if i > 2 * n :
            break

    print (count)
