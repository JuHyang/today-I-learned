def main () :
    N = int (input ())

    list_num = list ()
    list_result = list ()
    max_input = 0
    num_current = 0
    for i in range (N) :
        input_num = int (input ())

        while num_current < input_num :
                num_current += 1
                list_num.append(num_current)
                list_result.append("+")

        if list_num[-1] == input_num :
            list_num.pop()
            list_result.append("-")

        else :
            print ("NO")
            return

    for i in list_result :
        print (i)

main ()
