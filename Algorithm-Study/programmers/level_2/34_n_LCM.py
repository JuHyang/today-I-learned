def GCD (a, b) :
    if a > b :
        return GCD (b, a)
    
    if a == 0 :
        return b
    
    return GCD (b % a, a)

def solution(arr):
    answer = 0

    while len(arr) != 1 :
        temp = GCD (arr[0], arr[1])
        arr.append(arr.pop(0) * arr.pop(0) // temp)

    answer = arr[0]
    return answer