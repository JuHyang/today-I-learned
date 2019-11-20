def solution(arr):
    answer = arr.copy()
    if len (arr) == 1:
        return [-1]

    min_num = min (answer)
    min_index = answer.index(min_num)
    answer.pop(min_index)
    return answer