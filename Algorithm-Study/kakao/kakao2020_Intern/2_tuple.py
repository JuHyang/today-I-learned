def solution(s):
    answer = []

    strInput = s[1:-1]

    status = False
    temp = []
    tempChar = ""

    listInput = []

    for char in strInput :
        if char == '{' :
            status = True
            continue

        if char == '}' :
            temp.append(int (tempChar))
            status = False
            listInput.append(temp)
            temp = []
            tempChar = ''
            continue

        if status == True :
            if char == ',' :
                temp.append(int (tempChar))
                tempChar = ''
            else :
                tempChar += char

    listInput.sort(key = lambda tuple : len (tuple))

    for tuple in listInput :
        for num in tuple :
            if num not in answer :
                answer.append(num)
                break


    return answer