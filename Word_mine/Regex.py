mport re
import os

dir_name = 'C:/Users/Alex/Desktop/Folder'

def regex(filename):

    new_file = filename[:-4] + 'new.ass'
    # Убрать шапку и добавить  брейк
    with open(filename, "r+", encoding='utf-8') as f:
        file = f.readlines()[17:]
        with open(new_file, 'w', encoding='utf-8') as ff:
            for i in file:
                ff.write("%s\n" % i)
                with open(new_file, 'a+', encoding='utf-8') as fff:
                    fff.write('\n')
    # Мув 1
    with open(new_file, 'r+', encoding='utf-8') as r:
        content = r.read()
        with open(new_file, 'w', encoding='utf-8') as rr:
            content = rr.write(re.sub(r'Dialogue:(.*?)Default,(.*),,(.*?)\n', '\\2:\\3\\n', content))
    # Мув 2
    with open(new_file, 'r+', encoding='utf-8') as rrr:
       content = rrr.read()
       with open(new_file, 'w', encoding='utf-8') as r4:
        r4.write(re.sub(r'(.*?) .,..............:(.*?)\n', '\\1: \\2', content))
    # Мув 3
    with open(new_file, 'r+', encoding='utf-8') as r5:
       content = r5.read()
       with open(new_file, 'w', encoding='utf-8') as r6:
        r6.write(re.sub(r'Оператор:.*', '', content))

    os.remove(filename)


for filename in os.listdir(dir_name):
    regex(filename)

