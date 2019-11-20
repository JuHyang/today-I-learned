def solution(nums):
    answer = 0
    temp = sorted(nums)
    count = 1
    for i in range (1, len(temp)) :
        if temp[i - 1] != temp[i] :
            count += 1
    answer = min (count, len(nums) // 2)
    return answer