T = int (input())

list_prime = [2]

for i in range (3, 10001) :
    for j in list_prime :
        if j ** 2 > i :
            list_prime.append(i)
            break
        if i % j == 0 :
            break

for i in range (T) :
    n = int (input ())

    list_temp = []
    list_temp_2 = []

    for j in range (int (n / 2)) :
        if int (n / 2) - j in list_prime and int (n / 2) + j in list_prime :
            print (int (n / 2) - j, int (n / 2) + j)
            break
