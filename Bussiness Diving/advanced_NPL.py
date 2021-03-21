# importing the module
import json
import re
from collections import Counter
import nltk

nltk.download('stopwords')
# from nltk.corpus import stopwords
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
             'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than', '"had']
snowball = SnowballStemmer(language="english")
json_file = 'buffer.json'
TOP = 10  # кол-во токенов для определения семантики

with open('corpus.txt', 'w+', encoding='utf-8') as c:
    with open(json_file, encoding='utf-8') as f:  # Допустим, открыли JSON как словарь
        data = f.read()
        comment_list = re.findall(".*\"content\":.(.*)", data, re.MULTILINE)
        #comment_list = re.sub(r"\'|\"|\\", '', comment_list, 0, re.MULTILINE)

        value_list = re.findall(".*\"thumbsUpCount\":.(.\d*)", data, re.MULTILINE)
        dictionary = dict(zip(comment_list, value_list))
        step = 0
        for line in comment_list:  # для каждого коммента вывести топ Х слов
            line = re.sub(r"\'|\"|\\\\", '', line, 0, re.MULTILINE)
            line = re.sub(r"[,.:]", "", line, 0)
            step += 1
            split_it = line.split()  # превращаю строку в массив [слово, слово, ...]
            j = len(split_it)
            i = 0
            while i < j:
                z = split_it[i]
                if z.lower() in stopwords:
                    split_it.pop(i)
                    j -= 1
                else:
                    split_it[i] = snowball.stem(z)  # теперь стемирование прям в цикле (урезаю слово до сволоформы)
                    i += 1
            # print(split_it)
            z = Counter(split_it).most_common(TOP)  # вывожу массив [(словоформа1, разы), ..., (словоформаTOP, разы)]
            # print(z)
            z_list = [list(elem) for elem in z]

            for n in z_list:  # использую лайки в качестве подтверждения правдивости интента

                for m in n:
                    # print(n[1])
                    q = (n[1] + int(value_list[step - 1]))/2
                    w = n[0] + ' '
                    c.writelines(w * round(q))
                # c.writelines(str(n))
            print(z_list)


"""def corpus_creator(list_of_lists, drop):
    corpus = []
    with open(drop, "w+", encoding='utf-8') as d:
        for i in list_of_lists:
            corpus.append(i[0] * i[1])
        d.writelines(corpus)"""
