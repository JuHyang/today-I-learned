def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees :
        index = 0
        for j in i :
            if j in skill :
                if j == skill[index] :
                    index += 1
                else :
                    answer -= 1
                    break
            
        answer += 1
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print (solution (skill, skill_trees))