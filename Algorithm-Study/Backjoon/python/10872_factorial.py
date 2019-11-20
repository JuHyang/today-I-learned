N = int (input ())

if N == 0 :
    print (1)

else :
    listResult = []
    for i in range (N) :
        if i == 0 :
            listResult.append(1)
        else :
            listResult.append(listResult[i - 1] * (i + 1))


    print (listResult[-1])