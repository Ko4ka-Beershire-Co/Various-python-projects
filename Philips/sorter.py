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

    i = np.array(i).flatten()  # Transform 2D list into 1D

    print(i)  # Все экстеншены

    print(set(i))  # Уникальные экстеншены

get_agent_extensions(audio)
