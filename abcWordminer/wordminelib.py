# Libs  for installing the LIBS
import codecs
import subprocess
import sys

# Dependencies - то, без чего не будет работать
import os
import re
from string import punctuation
import pandas as pd

from collections import Counter

DEPENDENCIES = ['nltk', 'collections', 'seaborn']

RUSSIAN_STOPWORDS = ['и', 'в', 'во', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так',
                     'его', 'но', 'да', 'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было',
                     'вот', 'от', 'меня', 'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда', 'даже', 'ну', 'вдруг',
                     'ли',
                     'если', 'уже', 'или', 'быть', 'был', 'него', 'до', 'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь',
                     'там',
                     'потом', 'себя', 'ей', 'может', 'они', 'тут', 'где', 'есть', 'надо', 'ней', 'для', 'мы', 'тебя',
                     'их', 'чем', 'была', 'сам', 'чтоб', 'без', 'будто', 'чего', 'раз', 'тоже', 'себе', 'под', 'будет',
                     'ж',
                     'тогда', 'кто', 'этот', 'того', 'потому', 'этого', 'какой', 'совсем', 'ним', 'здесь', 'этом',
                     'один',
                     'почти', 'мой', 'тем', 'чтобы', 'нее', 'сейчас', 'были', 'куда', 'зачем', 'всех', 'можно',
                     'при', 'наконец', 'два', 'об', 'другой', 'хоть', 'после', 'над', 'больше', 'тот', 'через', 'эти',
                     'нас',
                     'про', 'всего', 'них', 'какая', 'много', 'разве', 'три', 'эту', 'моя', 'впрочем', 'свою', 'этой',
                     'перед', 'иногда', 'лучше', 'чуть', 'том', 'нельзя', 'такой', 'им', 'более', 'всегда', 'конечно',
                     'всю', 'между', 'аллё', '']


def install_dependencies(dependencies):
    for package in dependencies:
        subprocess.run(["pip", "install", package])
    print("Dependencies have been installed successfully.")


def phrase_extractor(ass_list, target_phrase_segment, look_forward, target_channel):
    current_iter = []  # Fix 2.0
    target_list = []
    target_list_id = []  # 2.0

    for i in ass_list:
        with open(f'./ASS_Files/{i}', 'r+', encoding='utf-8') as subtitle:
            lines = subtitle.readlines()
            for j in lines:
                # Ищем строку, где упомянут сегмент целевой фразы
                if target_phrase_segment in j:
                    call_id = lines[1][7:-1]
                    occurrence = lines.index(j)
                    x = 1

                    # Проверяем транскрипцию на look_forward вперед, и забираем строки из канала target_channel
                    current_iter = []
                    while x <= look_forward:
                        try:
                            check = lines[occurrence + x]

                        except IndexError:
                            # print('Out of Range')
                            pass

                        # Если мы метчим фразу, то нужно произвести с ней nltk-манипуляции++ и засунуть в финальный
                        # корпус
                        if target_channel in check:
                            words = re.findall(r",,(.*?$)", str(check))[0]
                            current_iter.append(words)
                        x += 1

                    target_list.append(current_iter)  # Fix 2.0
                    target_list_id.append(call_id)  # 2.0
                else:
                    pass
    output = {
        'Phrases': target_list,
        'Call_id': target_list_id
    }
    return output


def phrase_extractor_lookback(ass_list, target_phrase_segment, look_back, target_channel):
    current_iter = []  # Fix 2.0
    target_list = []
    target_list_id = []  # 2.0

    for i in ass_list:
        with open(f'./ASS_Files/{i}', 'r+', encoding='utf-8') as subtitle:
            lines = subtitle.readlines()
            for j in lines:
                # Ищем строку, где упомянут сегмент целевой фразы
                if target_phrase_segment in j:
                    call_id = lines[1][7:-1]
                    occurrence = lines.index(j)
                    x = 1

                    # Проверяем транскрипцию на look_forward вперед, и забираем строки из канала target_channel
                    current_iter = []
                    while x <= look_back:
                        try:
                            check = lines[occurrence - x]

                        except IndexError:
                            # print('Out of Range')
                            pass

                        # Если мы метчим фразу, то нужно произвести с ней nltk-манипуляции++ и засунуть в финальный корпус
                        if target_channel in check:
                            words = re.findall(r",,(.*?$)", str(check))[0]
                            current_iter.append(words)
                        x += 1

                    target_list.append(current_iter)  # Fix 2.0
                    target_list_id.append(call_id)  # 2.0
                else:
                    pass
    output = {
        'Phrases': target_list,
        'Call_id': target_list_id
    }
    return output


def normalizer(target_list, russian_stopwords):
    final_list = []
    # Отрицательные частицы сшиваются со словами (Заранее прошу прощение у Рамзана NLP-спецов)
    # Все слова из предыдущего списка выносятся из простыни
    for i in target_list:
        temp = ''
        for j in i:
            temp += f' {j}'
        temp = re.sub(r"( не) (.*?)", "\\1\\2", temp)
        temp = re.sub(r"( ни) (.*?)", "\\1\\2", temp)
        temp = temp.lower()
        for wor in russian_stopwords:
            try:
                temp = temp.replace(f' {wor} ', ' ')
            except:
                pass

        final_list.append(temp)

    return final_list


def create_txt_file(final_list, target_list_id):
    file_name = 'выгрузка'  # придумываем название, упадет в корневую папку

    with open(f'./{file_name}.txt', 'w+', encoding='utf-8') as cd:
        for index, line in enumerate(final_list):
            cd.write(f'{target_list_id[index]}\t{index}\t{line}\n')
    print('Выгрука готова')


def print_output_console(final_list, target_list_id):
    # В принципе, контрол+С -> контрол+V можно и отсюда...
    for index, line in enumerate(final_list):
        print(f'{target_list_id[index]}\t{index}\t{line}')


def count_top_occurrences(final_list, topx):
    full_canvas = ''
    for i in final_list:
        full_canvas += f' {i}'

    list_canvas = full_canvas.split()

    counter = Counter(list_canvas)
    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = counter.most_common(topx)
    print(most_occur)
    return most_occur


def create_occur_plot(most_occur):
    import seaborn as sns
    xes = []
    ys = []
    topx = len(most_occur)

    for i in most_occur:
        xes.append(i[0])
        ys.append(i[1])

    total = {
        'X': xes,
        'Y': ys
    }

    plt = sns.barplot(data=total, x='X', y='Y', orient="v")
    plt.set_xticklabels(
        labels=xes, rotation=60)

    print(f'Топ {topx} слов в выборке:')


def create_csv_output(final_list, target_list_id, file_name='выгрузка', separator=','):
    with open(f'./{file_name}.csv', 'w+', encoding="utf-8-sig") as output:
        output.write(f'call_id{separator}'
                     f'call_date{separator}'
                     f'robot_version{separator}'
                     f'log_item_index{separator}'
                     f'time_since_call_start{separator}'
                     f'source_state{separator}'
                     f'top_hypothesis\n')
        for index, line in enumerate(final_list):
            output.write(f'{target_list_id[index]}{separator}'
                         f'01/01/1900{separator}'
                         f'{separator}'
                         f'1{separator}'
                         f'00:00:10{separator}'
                         f'answer_talk_right_now{separator}'
                         f'{line}\n')
    print('Выгрузка готова')
