input_str = input ()
list_input = input_str.split()
N = int (list_input[0])
M = int (list_input[1])

result = "<"

list_num = []
for i in range (N) :
    list_num.append(i + 1)
i = 0
while len(list_num) != 0 :
    i = i + M - 1
    while i >= len (list_num) :
        i -= len (list_num)
    result += str (list_num.pop(i))

    if len (list_num) != 0 :
        result += ", "

result += ">"

print (result)
