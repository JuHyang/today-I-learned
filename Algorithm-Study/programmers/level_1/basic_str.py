def solution(s):
    length = len (s)
    if length != 4 and length != 6 :
        return False

    try :
        temp = int (s)
        return True
    except :
        return False
    