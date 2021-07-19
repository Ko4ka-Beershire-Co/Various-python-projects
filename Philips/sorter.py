import re
import shutil
import os
import numpy as np

audio = "C://Users/Alex/Desktop/Python/Markup/Philips Pipeline/Audio"  # all audio files

def get_agent_extensions(audio):
    i = []  # extensions
    j = []  # filename
    k = []  # 2D agent - name
    for filename in os.listdir(audio):
        j.append(filename)
        extension = re.findall(r'_(.*?)-', filename)
        i.append(extension)

    i = np.array(i).flatten()  # Transform 2D list into 1D

    # Создать словарь замены экстеншен - имя

    sorted_ext = ['101628', '101626', '101603', '101643', '101612', '101650', '101656', '101646', '101653', '101648',
                  '101627', '101630', '101614', '101658', '101602', '101616', '101649', '101624', '101634', '101609']

    sorted_names = ['Андрей Филипс', 'Дмитрий Филипс', 'Игорь Филипс', 'Юлия Филипс', 'Илья Филипс', 'Кристина Филипс',
                    'Илья2 Филипс', 'Дмитрий2 Филипс', 'Татьяна Филипс', 'Кирилл Филипс', 'Наталья Филипс',
                    'Ирина Филипс', 'Елена Филипс', 'Александр Филипс', 'Юрий Филипс', 'Виктория Филипс',
                    'Анна Филипс', 'Максим Филипс', 'Алена Филипс', 'Марина Филипс']

    # Создать соответствие экстеншен - звонок
    count = 0
    for value in j:
        l = []
        l.append(value)
        l.append(i[count])
        k.append(l)
        count += 1

    #print(i)  # Все экстеншены

    #print(set(i))  # Уникальные экстеншены

    #print(k)

    # Финальное соответствие:
    for pair in k:
        pair[1] = sorted_names[sorted_ext.index(pair[1])]

    print(k)
get_agent_extensions(audio)
