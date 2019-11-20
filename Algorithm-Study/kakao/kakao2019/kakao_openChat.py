class User :

    def __init__ (self, id, action) :
        self.id = id
        self.action = action

    def change (self, nickname) :
        self.nickname = nickname

def changeStr (list_user, dict_user) :
    list_result = []
    for i in list_user :
        str_result = ""
        if i.action == -1 :
            str_result += dict_user[i.id] + "님이 나갔습니다."
        elif i.action == 1 :
            str_result += dict_user[i.id] + "님이 들어왔습니다."

        list_result.append(str_result)
    return list_result

def solution(record):
    list_user = []

    dict_user = dict()


    for i in record :
        list_str = i.split()
        if list_str[0] == "Enter" :
            user_temp = User(list_str[1], 1)
            dict_user[list_str[1]] = list_str[2]
            list_user.append(user_temp)
        elif list_str[0] == "Leave" :
            user_temp = User(list_str[1], -1)
            list_user.append(user_temp)
        elif list_str[0] == "Change" :
            dict_user[list_str[1]] = list_str[2]


    answer = changeStr(list_user, dict_user)

    return answer
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = solution(record)
print (answer)
