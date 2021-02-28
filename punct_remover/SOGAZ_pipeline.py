import re
import os


def rem_punct(dir_name): # Я забыл как оно работает, главное, что работает выносит пунктуацию (27 строка)
    print('rem_punct---------|')
    for filename in os.listdir(dir_name):

        full_path = str(dir_name) + '/' # что os, что os.path в итирации любят абсолютный путь(((

        new_file = filename[:-4] + 'new.ass'

        # читаю тело (не .readlines())
        with open(full_path + filename, "r+", encoding='utf-8') as f:
            body_old = f.read()
            body = re.sub(r'(.*).Events].', '', body_old, re.MULTILINE, re.DOTALL) # отдельно тело
            # читаю шапку (не .readlines())
            with open(full_path + filename, "r+", encoding='utf-8') as t:
                top_old = t.read()
                top = re.sub(r'.Events](.*)', '[Events]\n', top_old, re.MULTILINE, re.DOTALL) # отдельно шапка
                top = re.sub(r'Title: (\d*)_(.*)', 'Title: '+ filename[:-4], top) # убрать суффикс
                top = re.sub(r'Audio File:(.*)_(.*).ogg', 'Audio File: ' + filename[:-4] + '.wav', top)  # убрать суффикс для .ogg (косяк с .wav)
                # Убираю пунктуацию из body 5 раз через loop
                j = 0
                while j < 8:
                    # r'(.*)[^\w\s](.*)' - внизу метчу все, кроме ?
                    body = re.sub(r'(.*)[.,!?:;(){}](.*)', "\\1\\2", body, 0, re.MULTILINE) # 0 - вводит глобалки (походу)
                    body = re.sub(r'Effect Text', 'Effect, Text', body, 0, re.MULTILINE)
                    body = re.sub(r"0000,0000,0000,", "0000,0000,0000,,", body, 0, re.MULTILINE)
                    body = re.sub(r"0000,0000,0000,,,", "0000,0000,0000,,", body, 0, re.MULTILINE)
                    j += 1

                    # Клею шапку и тело
                with open(full_path + new_file, 'a+', encoding='utf-8') as fff:
                    fff.write(body) #CR FT SOH STX CR LF Removal
                    print('Регулярки работают---|')
        # Удаляю первый файл и переименовываю второй
        os.remove(full_path + filename)
        os.rename(full_path + new_file, full_path + filename)
        print('Старый файл удален------|')
    print('Rem_punct отработал---------|')


def split_and_string(dir_name):  # Создает 2 txt-файла из 1 ass, для L и R каналов, и соединяет текст в один string
    #  L и R, естественно, перепутаны, решение - свап в именах: 73 и 77
    print('split_and_string---------|')
    for filename in os.listdir(dir_name):

        full_path = str(dir_name) + '/' # что os, что os.path в итирации любят абсолютный путь(((

        # читаю тело (не .readlines())
        with open(full_path + filename, "r+", encoding='utf-8') as f:
            old_LR = f.read()
            #  Для L канала 00
            L = re.sub(r'(.*)0,0000,0000,0000,,(.*)', "", old_LR, 0, re.MULTILINE)
            L = re.sub(r'(.*)1,0000,0000,0000,(.*)(\n*)', "\\2", L, 0, re.MULTILINE)
            L = re.sub(r',', " ", L, 0, re.MULTILINE)
            L = re.sub(r'.*\n', "Sentence =", L, 0, re.MULTILINE)
            L = re.sub(r'Sentence = ', "Sentence=", L, 0, re.MULTILINE)
            L = re.sub(r'Sentence =Sentence=', "Sentence=", L, 0, re.MULTILINE)  # Канальный хэндл
            # L = re.sub(r'(.*)', "\\1\r", L, 0, re.MULTILINE)
            print('Регулярки работают---|')
            #  Для R канала 01
            R = re.sub(r'(.*)1,0000,0000,0000,,(.*)', "", old_LR, 0, re.MULTILINE)
            R = re.sub(r'(.*)0,0000,0000,0000,(.*)(\n*)', "\\2", R, 0, re.MULTILINE)
            R = re.sub(r',', " ", R, 0, re.MULTILINE)
            R = re.sub(r'.*\n', "Sentence =", R, 0, re.MULTILINE)
            R = re.sub(r'Sentence = ', "Sentence=", R, 0, re.MULTILINE)
            R = re.sub(r'Sentence =Sentence=', "Sentence=", R, 0, re.MULTILINE)  # Канальный хэндл
            # R = re.sub(r'(.*)', "\\1\r", R, 0, re.MULTILINE)
            print('Регулярки работают---|')

            with open(full_path + filename[:-4] + 'r.txt', "a", encoding='utf-8',) as L_txt:
                L_txt.write(L + '\n')
                L_txt.close()
                print('L создан------|')
            with open(full_path + filename[:-4] + 'l.txt', "a", encoding='utf-8') as R_txt:
                R_txt.write(R + '\n')
                R_txt.close()
                print('R создан------|')

        os.remove(full_path + filename) # Удаляем ass-файл

        print('ass отработан------|')

    print('split_and_string отработал---------|')

rem_punct('SOGAZ_test')
split_and_string('SOGAZ_test')
