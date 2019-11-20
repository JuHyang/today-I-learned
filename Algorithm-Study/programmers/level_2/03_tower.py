def solution(heights):
    answer = [0]
    for i in range (1, len (heights)) :
        for j in range (1, i + 1) :
            if heights[i] < heights[i - j] :
                answer.append(i - j + 1)
                break
            elif i == j :
                answer.append(0)
    return answer

heights = [6, 9, 5, 7, 4]
print (solution (heights))