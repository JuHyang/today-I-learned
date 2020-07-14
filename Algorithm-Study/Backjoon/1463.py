result_list = [0, 0]

def func (x) :
    global result_list
    start = 2
    while start <= x :
        temp = 1
        if start % 2 != 0 and start % 3 != 0 :
            temp += result_list[start - 1]
            result_list.append(temp)
        else :
            if start % 3 == 0 :
                a = temp + result_list[int (start / 3)]
                b = temp + result_list[start - 1]
                temp = min (a, b)
                result_list.append(temp)
            elif start % 2 == 0:
                a = temp + result_list[int (start / 2)]
                b = temp + result_list[start - 1]
                temp = min(a, b)
                result_list.append(temp)
        start += 1
    return result_list[x]

def main () :
    x = int (input ())

    result = func (x)

    print (result)

main()