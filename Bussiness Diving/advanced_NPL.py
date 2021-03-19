# importing the module
import json
import re
from collections import Counter
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

stopwords.words("english")
snowball = SnowballStemmer(language="english")
json_file = 'buffer.json'

with open(json_file, encoding='utf-8') as f:  # Допустим, открыли JSON как словарь
    data = f.read()
    comment_list = re.findall(".*\"content\":.(.*)", data, re.MULTILINE)

    value_list = re.findall(".*\"thumbsUpCount\":.(.\d*)", data, re.MULTILINE)

    dictionary = dict(zip(comment_list, value_list))

    for line in comment_list:  # для каждого коммента вывести топ Х слов
        split_it = line.split()
        for i in split_it:
            for j in i:
                snowball.stem(i)
        j = Counter(split_it).most_common(5)
        print(j)
