str_input = input()
list_input = str_input.split()
list_difficulty = []

N = int (list_input[0])
L = int (list_input[1])
K = int (list_input[2])

for i in range (N) :
    str_input = input()
    list_input = str_input.split()
    temp = []
    temp.append (int (list_input[0]))
    temp.append (int (list_input[1]))
    list_difficulty.append(temp)

count_solved = 0
result = 0
index = 0
while index < len(list_difficulty) :
    if count_solved == K :
        break
    if (list_difficulty[index][1] <= L) :
        count_solved += 1
        result += 140
        list_difficulty.pop(index)
        continue
    index += 1

if count_solved != K :
    for i in list_difficulty :
        if count_solved == K :
            break
        if i[0] <= L :
            count_solved += 1
            result += 100

    
print(result)