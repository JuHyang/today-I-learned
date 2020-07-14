N = int (input ())
list_hum = []
list_rank = []
for i in range (N) :
    str_input = input()
    list_input = str_input.split()
    temp = []
    temp.append(int (list_input[0]))
    temp.append(int (list_input[1]))
    list_hum.append(temp)
    list_rank.append(1)

for i in range (N - 1) :
    first = list_hum[i]
    for j in range (i + 1, N) :
        second = list_hum[j]

        if first[0] > second[0] and first[1] > second[1] :
            list_rank[j] += 1
        elif first[0] < second[0] and first[1] < second[1] :
            list_rank[i] += 1


result = ""
for i in list_rank :
    result += str(i) + " "

print (result)