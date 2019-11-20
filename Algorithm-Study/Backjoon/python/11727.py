list_result = [1, 1]
def func (x) :
    start = 2
    while start <= x :
        temp = 2 * list_result[start - 2] + list_result[start - 1]
        list_result.append(temp)
        start += 1
    return list_result[x] % 10007

def main () :
    x = int (input ())

    result = func (x)

    print (result)

    return 0
main ()