def judge (s) :
    count = 0
    for char in s :
        if char == '(' :
            count += 1
        else :
            if count < 1 :
                return False
            else :
                count -= 1
    return True

def balance (s) :
    left = 0
    right = 0
    count = 0
    for char in s :
        if char == '(' :
            left += 1
        else :
            right += 1
        count += 1
        if left == right :
            return count

def create (p) :
    if p == '' :
        return ''
    answer = ''
    cnt_balance = balance(p)
    u = p[:cnt_balance]
    v = p[cnt_balance:]
    if judge(u) :
        return u + create(v)

    if judge(v) == False and len(v) != 0 :
        v = create(v)

    answer = '('
    for i in range (1, len(u) - 1) :
        if u[i] == '(' :
            answer += ')'
        else :
            answer += '('
    answer += ')' + v
    return answer
    
def solution(p):
    answer = create(p)
    return answer