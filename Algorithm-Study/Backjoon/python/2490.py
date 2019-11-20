def solution (stick_list) : 
    count = 0
    for i in stick_list :
        if i == "0" :
            count += 1
    if count == 0 :
        return "E"
    elif count == 1 :
        return "A"
    elif count == 2 :
        return "B"
    elif count == 3 :
        return "C"
    elif count == 4 :
        return "D"


for i in range (3) :
    input_str = input ()
    stick_list = input_str.split()
    print (solution (stick_list))