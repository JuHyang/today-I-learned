N = int (input ())

result = ""
for i in range (1, N + 1) :
    temp = str(i)
    if '3' in temp or '6' in temp or '9' in temp :
        temp = "-" * (temp.count('3') + temp.count('6') + temp.count('9'))
    
    result += temp

    if i != N :
        result += ' '

print (result)
