M = int (input ())
N = int (input ())

count = 0

list_result = []

for i in range (M , N + 1) :
    if i == 0 or i == 1 :
        continue
    if i == 2 :
        list_result.append(i)
        continue
    if i > 2 :
        for j in range (2, i) :
            if j ** 2 > i :
                list_result.append(i)
                break

            if i % j == 0 :
                break
if len (list_result) != 0 :
    print (sum (list_result))
    print (min (list_result))
else :
    print (-1)
