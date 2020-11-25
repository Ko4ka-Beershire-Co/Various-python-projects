import re
import os

run = 'C:/Users/Alex/Desktop/Folder'

def rem_punct(dir_name):

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
                top = re.sub(r'Audio File:(.*)_(.*).ogg', 'Audio File: ' + filename[:-4] + '.ogg', top)  # убрать суффикс для .ogg
                # Убираю пунктуацию из body 5 раз через loop
                j = 0
                while j < 5:
                    # r'(.*)[^\w\s](.*)' - внизу метчу все, кроме ?
                    body = re.sub(r'(.*)[.,!:;(){}](.*)', "\\1\\2", body, 0, re.MULTILINE) # 0 - вводит глобалки (походу)
                    body = re.sub(r'Effect Text', 'Effect, Text', body, 0, re.MULTILINE)
                    body = re.sub(r"0000,0000,0000,", "0000,0000,0000,,", body, 0, re.MULTILINE)
                    body = re.sub(r"0000,0000,0000,,,", "0000,0000,0000,,", body, 0, re.MULTILINE)
                    j = j + 1

                    # Клею шапку и тело
                with open(full_path + new_file, 'a+', encoding='utf-8') as fff:
                    fff.write(top + body) #CR FT SOH STX CR LF Removal
                    print('Регулярки работают---|')
        # Удаляю первый файл и переименовываю второй
        os.remove(full_path + filename)
        os.rename(full_path + new_file, full_path + filename)
        print('Старый файл удален------|')


# итиративная для папок 00-nn

start = 0
stop = 1 # №-1

while start < stop:

# Counter for 00-15
    if start < 10:
        sub_dir = '0' + str(start)
    elif start >= 10:
        sub_dir = str(start)

    run_new = str(run) + '/' + str(sub_dir) # так можно на глубину уйти

    rem_punct(run_new)

    start = start + 1
    print('Loop No ' + str(start) + ' работает---------|')
