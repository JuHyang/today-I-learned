input_str = input ()
input_str = input_str.upper()
spell_dict = dict()
for i in input_str :
    if i in spell_dict :
        spell_dict[i] += 1
    else :
        spell_dict[i] = 1

count_list = list (spell_dict.values())


max = 0

for k, v in spell_dict.items() :
    if v > max :
        max = v
        result = k

if count_list.count(max) > 1 :
    result = "?"

print (result)
