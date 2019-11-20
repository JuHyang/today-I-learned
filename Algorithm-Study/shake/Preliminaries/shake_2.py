str_input = input ()
list_input = str_input.split()

A = int (list_input[0])
B = int (list_input[1])
N = int (list_input[2])

list_order = []

for i in range (N) :
    str_input = input()
    list_input = str_input.split()
    temp = []
    temp.append(int (list_input[0]))
    temp.append(list_input[1])
    temp.append(int (list_input[2]))
    list_order.append(temp)

present_count = 1
count_B = 0
count_R = 0
result_B = ""
result_R = ""
for i in list_order :
    if i[1] == "B" :
        for j in range (i[2]) :
            count_B += 1
            result_B += str (present_count) + " "
            present_count += 1
    if i[1] == "R" :
        for j in range (i[2]) :
            count_R += 1
            result_R += str (present_count) + " "
            present_count += 1

print (count_B)
print (result_B)
print (count_R)
print (result_R)