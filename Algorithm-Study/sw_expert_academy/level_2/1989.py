T = int (input ())
for i in range (T) :
    str_input = input()

    result = "1"
    for j in range (len (str_input) // 2 + 1) :
        if str_input[j] != str_input[- (j + 1)] :
            result = "0"
            break

    print ("#" + str(i + 1) + " " + result)