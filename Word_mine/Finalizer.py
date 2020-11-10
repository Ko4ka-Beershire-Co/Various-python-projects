import re
from collections import Counter
# connect не + cлово
file_name = 'BIG_FILE.txt'

with open(file_name, 'r+', encoding='utf-8') as r:
    content = r.read()
    with open(file_name, 'w', encoding='utf-8') as rr:
        rr.write(re.sub(r' не ', ' не', content))

with open(file_name, "r+", encoding='utf-8') as ff:
    data_set = ff.read()
    # split() returns list of all the words in the string
    split_it = data_set.split()

    # Pass the split_it list to instance of Counter class.
    Counter = Counter(split_it)

    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = Counter.most_common(50)

    print(most_occur)

# Count
"""with open(file_name, "r+", encoding='utf-8') as ff:
    file = ff.read()
    word_list = file.split()
    word_freq = []
    for w in word_list:
        word_freq.append(word_list.count(w))

    #print(word_list)
    #print (word_freq)

    #print("String\n" + word_string + "\n")
    #print("List\n" + str(word_list) + "\n")
    #print("Frequencies\n" + str(word_freq) + "\n")
    with open('log.txt',"w+") as l:
        l.write("Pairs\n" + str(list(zip(word_list, word_freq))))
        with open('log.txt','a+') as ll:
            (word_freq.sort())
            ll.write(str(word_freq[-50:]))"""
