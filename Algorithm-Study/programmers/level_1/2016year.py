def solution(a, b):
    answer = ''
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    mon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    day_result = sum(mon[:a]) + b - 1
    answer = day[(day_result % 7 + 5) % 7]

    return answer