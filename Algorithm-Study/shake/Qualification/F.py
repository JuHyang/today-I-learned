input_str = input ()
input_list = input_str.split()

N = int (input_list[0])
w = int (input_list[1])

list_candy3 = []
list_candy5 = []
for i in range (N) :
    input_str = input()
    input_list = input_str.split()

    temp = []
    if int (input_list[0]) == 3 :
        list_candy3.append(int (input_list[1]))
    else :
        list_candy5.append(int (input_list[1]))

list_candy3.sort()
list_candy5.sort()

print (list_candy3)
print (list_candy5)

