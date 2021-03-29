import re
import os

error_file_path = "C://Users/Alex/Desktop/Python/Markup/Error_finder/Errors"
# script_path = "C://Users/Alex/Desktop/Python/Markup/Error_finder"
file_names = []

for filename in os.listdir(error_file_path):

    with open(error_file_path + '/' + filename, 'r+', encoding='utf-8', ) as f:
        body = f.read()
        error_list = re.findall(r'\"filename\": \"(.*)\"', body, re.MULTILINE)
        file_names.append(set(error_list))

print(file_names)
