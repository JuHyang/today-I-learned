def permutation (length) :
    result = length
    for i in range (length - 1) :
        temp = length
        for j in range (i) :
            temp *= length - j
        result += temp
    print (result)
    return result

N = int (input ())

word_n = []
word_c = []
word_nc = []
word_cn = []

for i in range (N) :
    input_str = input()
    category = 0
    for j in input_str :
        if category == 0 :
            if j == "N" :
                category = 1
            elif j == "C" : 
                category = 3
        
        elif category == 1 or category == 4 :
            if j == "C" :
                category = 2
                break
        elif category == 3 :
            if j == "N" :
                category = 4

    if category == 1 :
        word_n.append(input_str)
    elif category == 2 :
        word_nc.append(input_str)
    elif category == 3 :
        word_c.append(input_str)
    elif category == 4 :
        word_cn.append(input_str)

print (word_n)
print (word_c)
print (word_nc)
print (word_cn)

a = permutation (len (word_n))
b = permutation (len (word_c))
c = permutation (len (word_nc))
d = permutation (len (word_cn))

print (a, b, c, d)
result = a * b + a * c + b * c + a * d + c * d + c

print (result)
