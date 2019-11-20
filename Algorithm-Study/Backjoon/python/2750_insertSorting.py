## 삽입정렬
N = int (input ())

list_num = []

for i in range (N) :
    temp = int (input ())
    if i == 0 :
        list_num.append(temp)
        continue
    for j in range (len (list_num)) :
        if list_num[j] > temp :
            list_num.insert(j, temp)
            break
        if j == len (list_num) - 1 :
            list_num.append(temp)

for i in list_num :
    print (i)
