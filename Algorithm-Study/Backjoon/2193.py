list_result = []
list_temp = [0, 1]

n = int (input ())

list_result.append(list_temp)


for i in range (n - 1) :
    list_result.append(list())

for i in range (1, n) :
    for j in range (2) :
        if j == 0 :
            temp = list_result[i - 1][0] + list_result[i - 1][1]
            list_result[i].append(temp)
        else :
            temp = list_result[i-1][0]
            list_result[i].append(temp)

print (sum (list_result[n-1]))