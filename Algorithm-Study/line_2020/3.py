def solution(n):
    answer = []

    if n < 10:
        return [0, n]

    strNum = str(n)
    count = 0

    while len(strNum) > 1:
        length = len(strNum) // 2
        while strNum[length] == '0':
            length += 1
        before = strNum[:length]
        after = strNum[length:]

        strNum = str(int(before) + int(after))
        count += 1

    return [count, int(strNum)]
