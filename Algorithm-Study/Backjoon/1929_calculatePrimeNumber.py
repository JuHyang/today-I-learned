str_num = input ()

list_num = str_num.split()

M = int (list_num[0])
N = int (list_num[1])

list_prime = [2]

for i in range (1 , N + 1) :

    if i == 0 or i == 1 :
        continue
    if i == 2 and i > M:
        print (2)
        continue
    if i > 2 :
        for j in list_prime :
            if j ** 2 > i :
                list_prime.append(i)
                if i >= M :
                    print (i)
                break

            if i % j == 0 :
                break
