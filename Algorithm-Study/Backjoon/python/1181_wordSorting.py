import sys
N = int (sys.stdin.readline())

dict_word = dict()
list_len = list()

for i in range (N) :

    word = sys.stdin.readline()
    word = word[:-1]
    len_word = len (word)

    if not len_word in list_len :
        list_len.append(len_word)

    if len_word in dict_word :
        temp_list = dict_word[len_word]
        if not word in temp_list :
            temp_list.append(word)
    else :
        dict_word[len_word] = []
        dict_word[len_word].append (word)

list_len.sort()
for i in dict_word.keys() :
    dict_word[i].sort()

for i in list_len :
    for j in dict_word[i] :
        print (j)
