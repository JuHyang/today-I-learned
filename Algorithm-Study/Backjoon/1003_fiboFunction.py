T = int (input ())
for i in range (T) :
    fibo_list = [[1, 0], [0, 1]]
    N = int (input ())
    
    if N < 2 :
        print (fibo_list[N][0], fibo_list[N][1])
        continue
    
    for j in range (2, N + 1) :
        countZero = fibo_list[j - 2][0] + fibo_list[j - 1][0]
        countOne = fibo_list[j - 2][1] + fibo_list[j - 1][1]
        fibo_list.append([countZero, countOne])
    
    print (fibo_list[-1][0], fibo_list[-1][1])
