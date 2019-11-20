list_result = []
list_1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

list_result.append(list_1)

n = int (input ())

for i in range (n - 1) :
    list_result.append(list())

for i in range (1, n) :
    for j in range (10) :
        if j == 0 :
            temp = list_result[i-1][1]
            list_result[i].append(temp)
        elif j == 9 :
            temp = list_result[i-1][8]
            list_result[i].append(temp)
        else :
            temp = list_result[i-1][j-1] + list_result[i-1][j+1]
            list_result[i].append(temp)

result = sum (list_result[n-1])
print (result % 1000000000)
