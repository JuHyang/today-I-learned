def printArr (arr, direction) :
    result = "["
    length = len (arr)
    if length == 0 :
        print ("[]")
        return
    if direction == 1 :
        for i in range (length) :
            if i == length - 1 :
                result += arr[i] + "]"
                break
            result += arr[i] + ","
    else :
        for i in range(1, length + 1):
            if i == length :
                result += arr[-i] + "]"
                break
            result += arr[-i] + ","
    print (result)

def main () :
    
    T = int (input ())

    for i in range (T) :
        error = 0
        p = input ()
        n = int (input ())
        input_arr = input ()
        
        input_arr = input_arr[1:-1]
        input_arr = input_arr.split(",")
        if input_arr[0] == '' :
            input_arr.pop()
        direction = 1

        for j in p :
            if j == "R" :
                direction *= -1
            if j == "D" :
                if len (input_arr) == 0 :
                    print ("error")
                    error = 1
                    break
                if direction == 1 :
                    input_arr.pop(0)
                elif direction == -1 :
                    input_arr.pop()
        if error == 1 :
            continue
        printArr (input_arr, direction)

main()
