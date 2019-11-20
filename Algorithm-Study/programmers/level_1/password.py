def solution(s, n):
    answer = ''
    list_lower = "abcdefghijklmnopqrstuvwxyz"
    list_upper = list_lower.upper()
    n = n % 26
    for char in s :
        if char == ' ' :
            answer += ' '
        elif char.islower() :
            index = list_lower.find(char) + n
            index = index % 26
            answer += list_lower[index]
        elif char.isupper() :
            index = list_upper.find(char) + n
            index = index % 26
            answer += list_upper[index]
    return answer