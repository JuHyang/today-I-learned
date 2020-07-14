n = int (input ())

triangle = []
for i in range (n) :
    input_str = input ()
    input_list = input_str.split()
    temp = []
    if i == 0 :
        temp.append(int (input_list[0]))
        triangle.append(temp)
        continue
    for j in range (len (input_list)) :
        if j == 0 :
            temp.append(triangle[i - 1][0] + int (input_list[0]))
        elif j == len (input_list) - 1 :
            temp.append(triangle[i - 1][-1] + int (input_list[-1]))
        else :
            temp.append(int (input_list[j]) + max (triangle[i - 1][j - 1], triangle[i - 1][j]))
    triangle.append(temp)

print (max (triangle[-1]))
