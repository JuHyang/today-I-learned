list_result = [1,1,2]

def func () :
    start = 3
    while start <= 11 :
        temp = list_result[start - 1] + list_result[start - 2] + list_result[start - 3]
        list_result.append(temp)
        start += 1
    return

def main() :
    func ()
    T = int (input())

    for i in range (T) :
        x = int (input ())
        print (list_result[x])

    return

main()