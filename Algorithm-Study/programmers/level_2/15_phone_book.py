def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key = lambda string : len (string))
    for i in range (len (phone_book)) :
        phone_num = phone_book[i]
        for j in range (i + 1, len (phone_book)) :
            if phone_num == phone_book[j][:len(phone_num)] :
                return False
    return answer