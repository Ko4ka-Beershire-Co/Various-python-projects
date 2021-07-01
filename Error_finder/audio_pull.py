import re
import os
import shutil


audio = "E://Записи/2ГИС"  # all audio files
txt = "C://Users/Alex/Desktop/Датасет эмоции/2ГИС"  # .txt names
# target = "C://Users/Alex/Desktop/Python/Markup/Error_finder/Target" # where do I put the missing files
# script_path = "C://Users/Alex/Desktop/Python/Markup/Error_finder"
file_names = []

for file in os.listdir(txt):
    # Get names
    for filename in os.listdir(txt + '/' + file):  # inside Emotion folder

        with open(txt + '/' + file + '/' + filename, 'r+', encoding='utf-8', ) as f:
            body = f.read()
            audio_file_name = re.findall(r'Звонок.(.*)_', body, re.MULTILINE)
            file_names.append(list(set(audio_file_name)))
    # Pull audio
    for i in file_names:
            
            shutil.move(audio + '/' + i, txt + '/' + file)


print(file_names)

"""def find_audio(list, folder, target):

    for i in list:
        for j in i:
            shutil.move(folder + '/' + j, target)

if __name__ == '__main__':

    find_audio(file_names,audio,target)"""
