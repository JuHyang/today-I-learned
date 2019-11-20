def solution(name):
    capital = ["A", "B", "C", "D", "E", "F", "G", "H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
    answer = 0
    for char in name :
        temp = capital.index(char)
        if temp > 13 :
            answer += 26 - temp
        else :
            answer += temp

    bool_list = []
    for i in range (len(name)) :
        if name[i] != 'A' :
            bool_list.append(i)
    
    index = 0
    while len (bool_list) != 0:
        temp = []
        for i in bool_list :
            a =  (abs (index - i))
            b =  (abs (len (name) + index - i))
            gab = min (a, b)
            temp.append(gab)
        index = temp.index(min(temp))
        index = bool_list.pop(index)
        answer += min(temp)
    return answer