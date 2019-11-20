N = int (input ())
if N == 1 :
    print (1)
elif N == 2 :
    print (2)
else :
    before = 1
    after = 2
    for i in range (3, N + 1) :
        temp = after
        after += before % 15746
        before = temp % 15746
    print (after % 15746)