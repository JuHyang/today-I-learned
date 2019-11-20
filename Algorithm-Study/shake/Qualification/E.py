def solution (N, M) :
    people = dict()
    doit = dict ()
    for i in range (M) :
        input_str = input ()
        input_list = input_str.split()

        f = int (input_list[0])
        b = int (input_list[1])

        if type(people.get(b)) == list :
            if f in people[b] :
                return False

        if doit.get(b) :
            continue

        if type(people.get(f)) == list :
            people[f].append(b)
        else :
            temp = [b]
            people[f] = temp
        doit[b] = 1

    if len(doit) != N :
        return False

    return True

input_str = input()
input_list = input_str.split()

N = int (input_list[0])
M = int (input_list[1])

if solution (N, M) :
    print ("YES")
else :
    print ("NO")
