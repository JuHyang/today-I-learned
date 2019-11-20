list_result = []
list_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

list_result.append(list_1)

n = int (input ())

for i in range (n - 1) :
    list_result.append(list())

for i in range (1, n) :
    for j in range (10) :
        if j == 0 :
            temp = 1
            list_result[i].append(temp)
        else :
            temp = list_result[i][j-1] + list_result[i-1][j]
            list_result[i].append(temp)

result = sum (list_result[n-1])
print (result % 10007)
