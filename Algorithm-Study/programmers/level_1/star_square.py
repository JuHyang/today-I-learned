a, b = map(int, input().strip().split(' '))
for i in range (b) :
    temp = ''
    for j in range (a) :
        temp += '*'
    print (temp)
