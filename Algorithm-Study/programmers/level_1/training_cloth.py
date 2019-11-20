def solution(n, lost, reserve):
    answer = 0
    clothes = []
    for i in range (n) :
        clothes.append(1)
    
    for i in lost :
        clothes[i - 1] -= 1

    for i in reserve :
        clothes[i - 1] += 1

    for i in range (len(clothes)) :
        if clothes[i] == 0 :
            if i != 0 :
                if clothes[i - 1] == 2 :
                    clothes[i - 1] = 1
                    clothes[i] = 1
                    continue

            if i != len (clothes) - 1 :
                if clothes[i + 1] == 2 :
                    clothes[i] = 1
                    clothes[i + 1] = 1
                    continue

    answer = len (clothes) - clothes.count(0)
    return answer