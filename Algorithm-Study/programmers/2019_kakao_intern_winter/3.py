from itertools import product  

def match (pattern, user) :
    if len (pattern) != len (user) :
        return False
    
    for i in range(len(pattern)) :
        if pattern[i] == user[i] or pattern[i] == "*" :
            continue
        else :
            return False
        
    return True
    

def solution(user_id, banned_id):
    answer = set()
    banList = []
    for ban_id in banned_id :
        tempList = []
        for user in user_id :
            if match(ban_id, user) == True : 
                tempList.append(user)
        banList.append(tempList)       
    
    
    productList = list(product(*banList))
    for banned in productList :
        if len(set(banned)) == len(banned_id) :
            answer.add("".join(sorted(set(banned))))
    return len(answer)