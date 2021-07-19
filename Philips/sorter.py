import re
import shutil
import os
import numpy as np

audio = "C://Users/Alex/Desktop/Python/Markup/Philips Pipeline/Audio"  # all audio files

def get_agent_extensions(audio):
    i = []
    for filename in os.listdir(audio):
        extension = re.findall(r'_(.*?)-', filename)
        i.append(extension)

    full_list = np.array(i).flatten()  # Transform 2D list into 1D

    unique_list = print(set(full_list))  # Уникальные экстеншены

    print(unique_list)
    #print(full_list)

get_agent_extensions(audio)
