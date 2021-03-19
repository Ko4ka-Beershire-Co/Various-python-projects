# importing the module
import json
import re
from collections import Counter
import nltk

nltk.download('stopwords')
#from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Важные переменные
stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during',
                   'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
                   'such', 'into', 'of',
                   'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
                   'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me',
                   'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both',
                   'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and',
                   'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
                   'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where',
                   'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 'it', 'being', 'if',
                   'theirs',
                   'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than','"had']
snowball = SnowballStemmer(language="english")
json_file = 'buffer.json'
TOP = 5  # кол-во токенов для определения семантики

with open(json_file, encoding='utf-8') as f:  # Допустим, открыли JSON как словарь
    data = f.read()
    comment_list = re.findall(".*\"content\":.(.*)", data, re.MULTILINE)

    value_list = re.findall(".*\"thumbsUpCount\":.(.\d*)", data, re.MULTILINE)
    dictionary = dict(zip(comment_list, value_list))

    for line in comment_list:  # для каждого коммента вывести топ Х слов
        split_it = line.split()  # превращаю строку в массив [слово, слово, ...]

        j = len(split_it)
        i = 0
        while i < j:
            z = split_it[i]
            if z.lower() in stopwords:
                split_it.pop(i)
                j -= 1
            else:
                i += 1

        for i in split_it:  # стемирую каждое слово: слово -> словоформа
            for j in i:
                snowball.stem(i)
        z = Counter(split_it).most_common(TOP)  # вывожу массив [(словоформа1, разы), ..., (словоформаTOP, разы)]
        step = 0
        for i in z:  # step - обходит tuple_index
            step += 1
            count = 0
            for j in i:
                count +=1
                if count %2 == 0:  # для каждого второго эл-та в j т.е. разов
                    j = j * int(value_list[step-1])  # домножу на кол-во лайков - лайкнул - согласен

        print(z)  # TOP словоформ для каждого коммента"""
