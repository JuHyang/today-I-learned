def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees :
        index = 0
        status = 0
        for s in tree :
            if s in skill :
                if s != skill[index] :
                    status = 1
                    break
                index += 1

        if status == 0 :
            answer += 1
    return answer