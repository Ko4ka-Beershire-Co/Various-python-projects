import re

with open ('import 275 - source data errors.json', 'r+', encoding='utf-8',) as f:
    body = f.read()
    error_list = re.findall(r'\"filename\": \"(.*)\"', body, re.MULTILINE)
    print(set(error_list))
