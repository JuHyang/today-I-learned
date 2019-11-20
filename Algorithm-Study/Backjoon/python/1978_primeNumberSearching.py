N = int (input ())

str_num = input ()

list_num = str_num.split()

count = 0

for i in range (N) :
    list_num[i] = int (list_num[i])

for i in list_num :
    if i == 0 or i == 1 :
        continue
    if i == 2 :
        count += 1
    if i > 2 :
        for j in range (2, i) :
            if j ** 2 > i :
                count += 1
                break

            if i % j == 0 :
                break

print (count)
