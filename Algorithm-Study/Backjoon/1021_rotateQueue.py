input_str = input ()
list_input = input_str.split()
N = int (list_input[0])
M = int (list_input[1])

input_str = input ()
list_input = input_str.split()
for i in range (M) :
    list_input[i] = int (list_input[i]) - 1

list_num = list ()

for i in range (N) :
    list_num.append(i)

index = 0
result = 0
for i in list_input :
    while True :
        if index < 0 :
            index += len (list_num)
        elif index >= len(list_num) :
            index -= len (list_num)
        if i == list_num[index] :
            list_num.pop(index)
            break
        else :
            if i > list_num[index] :
                right = list_num.index(i) - index
                left = index - list_num.index(i) + len (list_num)
            else :
                right = list_num.index(i) - index + len (list_num)
                left = index - list_num.index(i)

            if right < left :
                mv = right
            else :
                mv = -left

            index += mv
            result += abs (mv)


print (result)
