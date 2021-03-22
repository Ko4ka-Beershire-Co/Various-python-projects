import re
file_name = 'Okko.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    content = f.read()
    new_content = re.sub(r'[()[\]\']', '', content, 0, re.MULTILINE)
    new_content = re.sub(r'(\S*?),\s(\d*),', '\\1, \\2;', new_content, 0, re.MULTILINE)

    with open(file_name[:4] + '_csv.txt', 'w+', encoding='utf-8') as n:
        n.write(new_content)
