def push (x, arr) :
    arr.append(x)

def pop (arr) :
    if len(arr) == 0:
        print (-1)
        return arr
    else :
        temp = arr[0]
        print (temp)
        arr = arr[1:]
        return arr

def size (arr) :
    print (len(arr))

def empty (arr) :
    if len(arr) == 0 :
        print (1)
    else :
        print (0)

def front (arr) :
    if len (arr) == 0 :
        print (-1)
    else :
        print (arr[0])

def back (arr) :
    if len(arr) == 0 :
        print (-1)
    else :
        print (arr[-1])


def __main__ () :
    N = int (input ())
    arr = []
    for i in range (0, N) :
        order = input()
        if order[0:4] == "push" :
            push (int (order[5:]), arr)
        elif order[0:3] == "pop" :
            arr = pop (arr)
        elif order == "size" :
            size (arr)
        elif order == "empty" :
            empty (arr)
        elif order == "front" :
            front (arr)
        elif order == "back" :
            back (arr)
            


__main__()
