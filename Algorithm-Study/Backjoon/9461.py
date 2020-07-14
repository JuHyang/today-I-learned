T = int (input ())
for i in range (T) :
    padoban = [1, 1, 1, 2, 2]
    N = int (input ())
    if N < 5 :
        print (padoban[N-1])
    else :
        for i in range (6, N + 1) :
            padoban.append(padoban[-1] + padoban[-5])
        print (padoban[-1])