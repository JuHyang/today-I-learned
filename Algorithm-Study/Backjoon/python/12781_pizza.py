def ccw (x, y, z) :
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]
    x3 = z[0]
    y3 = z[1]
    result = ((x2 - x1) * (y3 - y1)) - ((y2 - y1) * (x3 - x1))
    if result > 0 :
        return 1
    elif result == 0 :
        return 0
    else :
        return -1

def check (a, b) :
    if a * b >= 0 :
        return False
    else :
        return True



input_str = input ()
list_input = input_str.split()
x1 = int (list_input[0])
y1 = int (list_input[1])

x2 = int(list_input[2])
y2 = int(list_input[3])

x3 = int(list_input[4])
y3 = int(list_input[5])

x4 = int(list_input[6])
y4 = int(list_input[7])

a = [x1, y1]
b = [x2, y2]
c = [x3, y3]
d = [x4, y4]

result1 = check (ccw (a, b, c), ccw (a, b, d))
result2 = check (ccw (c, d, a), ccw(c, d, b))

if result1 == True and result2 == True :
    print (1)
else :
    print (0)