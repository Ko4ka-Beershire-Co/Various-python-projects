import re


with open('metadata3.json', 'r+') as JSON:
    list_ext = re.findall(r'"extension": "(\d*?)"', str(JSON.read()), re.MULTILINE)

print(list_ext)

print(list(set(list_ext)))  # removes duplicates from a lest
