import re

def solution(user_id, banned_id):
    answer = 1

    listBan = []

    for ban in banned_id :
        banUser = ban.replace('*', '.')
        pattern = re.compile(banUser)
        temp = []
        for i in range (len (user_id)) :
            user = user_id[i]
            if len (user) == len (banUser) :
                result = pattern.match(user)
                if result :
                    temp.append(i)
        listBan.append(temp)

    print (listBan)

    for ban in listBan :
        print (ban)
    

    return answer