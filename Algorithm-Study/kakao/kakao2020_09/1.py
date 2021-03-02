import re


def solution(new_id):
    answer = ''

    temp = new_id.upper()
    pattern = "[^A-Za-z0-9\._-]"

    temp = re.sub("[^A-Za-z0-9\._-]", '', temp)
    temp = str(re.sub("[\.]+", '.', temp))

    while (len(temp) > 0 and temp[0] == '.'):
        temp = temp[1:]

    while (len(temp) > 0 and temp[-1] == '.'):
        temp = temp[:-1]

    if len(temp) == 0:
        temp = 'a'

    if len(temp) > 15:
        temp = temp[:15]
        while (len(temp) > 0 and temp[-1] == '.'):
            temp = temp[:-1]

    if len(temp) == 0:
        temp = 'a'

    while len(temp) < 3:
        temp += temp[-1]

    answer = temp.lower()

    return answer
