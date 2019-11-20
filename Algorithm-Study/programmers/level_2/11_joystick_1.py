def solution(name):
    capital = ["A", "B", "C", "D", "E", "F", "G", "H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
    answer = 0
    max_A = 0

    temp = [0] * len(name)
    for i in range (1, len (name)) :
        if name[i] == 'A' :
            temp[i] = temp[i - 1] + 1
        else :
            temp[i] = 0
    max_A = max (temp)

    for char in name :
        temp = capital.index(char)
        if temp > 13 :
            answer += 26 - temp
        else :
            answer += temp
    answer += len (name) - 1
    answer -= max_A
    return answer

print (solution ("AZAAAZ"))