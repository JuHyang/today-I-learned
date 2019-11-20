list_fib = [0, 1]

n = int (input ())

for i in range (2, n + 1) :
    temp = list_fib[i - 2] + list_fib[i - 1]
    list_fib.append(temp)

print (list_fib[-1])
