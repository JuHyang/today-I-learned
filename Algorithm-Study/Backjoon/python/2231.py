N = int (input ())

count = 1
result = 0
while count < N :
    temp = count
    temp1 = temp
    while temp != 0 :
        temp1 += temp % 10
        temp = temp // 10
    if temp1 == N :
        result = count
        break
    result = 0
    count += 1

print (result)