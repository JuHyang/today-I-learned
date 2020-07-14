list_fib = [0, 1]

n = int (input ())
temp = 2
while temp != n + 1 :
    list_fib.append(list_fib[0] + list_fib[1])
    list_fib.pop(0)
    temp += 1

print (list_fib[-1] % 1000000)
