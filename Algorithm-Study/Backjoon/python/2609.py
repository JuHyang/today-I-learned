def GCD (a, b) :
    if b == 0 :
        return a
    else :
        return GCD (b, a % b)

def solution (a, b) :
    input_a = a
    input_b = b
    if a < b :
        input_a = b
        input_b = a

    gcd = GCD (input_a, input_b)
    print (gcd)
    print (int (input_a / gcd) * int (input_b / gcd) * gcd)

input_str = input ()
input_list = input_str.split ()
solution (int (input_list[0]), int (input_list[1]))