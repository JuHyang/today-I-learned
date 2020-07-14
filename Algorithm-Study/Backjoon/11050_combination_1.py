inputStr = input ()
inputStr = inputStr.split()
N = int (inputStr[0])
K = int (inputStr[1])

top = 1
bottom = 1

for i in range (K) :
    top *= N - i

for i in range (1, K + 1) :
    bottom *= i
result = int (top/bottom)
print (result)