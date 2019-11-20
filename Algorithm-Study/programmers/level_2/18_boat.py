def solution(people, limit):
    answer = 0
    people.sort()
    small = 0
    big = len (people) - 1
    while small < big:
        if people[small] + people[big] <= limit :
            small += 1
            big -= 1
            answer += 1
        else :
            big -= 1
            answer += 1
        if small == big :
            answer += 1
    return answer