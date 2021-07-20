import re
import os
import shutil
import csv


audio = "C://Users/Alex/Desktop/Python/Markup/Philips Pipeline/Audio"  # all audio files
destination = "C://Users/Alex/Desktop/Python/Markup/Audio_Pull/Target"  # .txt names
error_list = []
# target = "C://Users/Alex/Desktop/Python/Markup/Error_finder/Target" # where do I put the missing files
# script_path = "C://Users/Alex/Desktop/Python/Markup/Error_finder"
file_names = []
stage = 1

"""for file in os.listdir(txt):
    # Get names
    for filename in os.listdir(txt + '/' + file):  # inside Emotion folder

        with open(txt + '/' + file + '/' + filename, 'r+', encoding='utf-8', ) as f:
            body = f.read()
            audio_file_name = re.findall(r'Звонок.(.*)_', body, re.MULTILINE)
            file_names.append(list(set(audio_file_name)))"""
    # Pull audio
    #  print(file_names)
with open ('Output.csv', newline='') as csv_file:
    spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')

    for i in spamreader:
        j = re.sub(r'Звонок\s(\d*_\d*-\d\d-\d\d-\d\d)','\\1.mp3', i[0], 0, re.MULTILINE)
        error_list.append(j)


for i in error_list:

    shutil.copy(audio + '/' + i, destination)
