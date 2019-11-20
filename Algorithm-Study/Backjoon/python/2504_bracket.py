def main () :
    input_str = input ()

    list_bracket = list ()
    result = 0
    list_temp = list ()
    i = 0
    while (i < len (input_str)) :

        if input_str[i] == '(' :
            if i == len (input_str) - 1:
                print (0)
                return
            if input_str[i+1] == ')' :
                i += 1
                temp = 2
                if len(list_temp) != 0 :
                    for j in list_temp :
                        temp *= j
                result += temp
            else :
                list_bracket.append('(')
                list_temp.append(2)
        elif input_str[i] == '[' :
            if i == len (input_str) - 1:
                print (0)
                return
            if input_str[i+1] == ']' :
                i += 1
                temp = 3
                if len (list_temp) != 0 :
                    for j in list_temp :
                        temp *= j
                result += temp
            else :
                list_bracket.append('[')
                list_temp.append(3)

        elif input_str[i] == ')' :
            if len(list_bracket) == 0 :
                print ('0')
                return
            if list_bracket[-1] != '(' :
                print ('0')
                return
            else :
                list_bracket.pop()
                list_temp.pop()

        elif input_str[i] == ']' :
            if len(list_bracket) == 0 :
                print ('0')
                return
            if list_bracket[-1] != '[' :
                print ('0')
                return
            else :
                list_bracket.pop()
                list_temp.pop()

        i += 1


    if len (list_bracket) != 0 :
        print (0)
        return
    print (result)

main ()
