import re
import sys
from pydub import AudioSegment
import itertools
import os
import shutil

dictionary = ['Михайловича', "могу услышать", "могу услышать", "Здравствуйте", "здравствуйте", "Компания", "меня зовут",
              "Слушаю"]


def obezlichit(audio_path, output_path):
    # filename section
    audio_path = audio_path[:-3] + 'mp3'
    sub_path = audio_path[:-3] + 'ass'

    with open(sub_path, 'r+', encoding='utf-8') as sub:
        body = sub.read()
        # lines to get timings from
        lines = []
        f_lines = []

        for i in dictionary:
            body_processed = re.findall(f'.*?{i}', body, re.MULTILINE)

            if body_processed:
                # print(body_processed[0])
                timing = re.findall(r'Dialogue:.(.*?),Default', body_processed[0])
                # print(timing[0])

                lines.append(timing[0][2:])

        for j in lines:
            # print(j)
            first = int(j[2:4]) * 60 * 1000 + int(j[5:7]) * 1000 + int(j[8:10]) * 10

            second = int(j[13:15]) * 60 * 1000 + int(j[16:18]) * 1000 + int(j[19:21]) * 10

            q_lines = [first, second]

        f_lines.append(q_lines)

        # Remove duplicates

        f_lines.sort()
        f_lines = list(k for k, _ in itertools.groupby(f_lines))
        # f_lines = list(set(f_lines))
        # f_list = list(dict.fromkeys(f_lines))

        # print(f_lines)

        new_list = [2000]

        for k in f_lines:
            for l in k:
                new_list.append(l)
        # Sort
        new_list.sort()

        # print(new_list)
        # print(len(new_list))

        target_list = []
        count = 0
        while count < len(new_list) - 1:
            timeframe = f'audio_file[{new_list[count]}:{new_list[count + 1]}]+'
            # print(timeframe)
            count += 1

            target_list.append(timeframe)

        pre_final = target_list[::2]

        pre_final.append(f'audio_file[{str(new_list[len(new_list) - 1])}:]')

        # print(pre_final)

        final = ''

        for n in pre_final:
            final += n

        # print(final)

        # Cut file part

        audio_file = AudioSegment.from_mp3(audio_path)

        code_string = f'audio_file = {final}\n'
        code_string_2 = f'audio_file.export(output_path, format="mp3")'
        print(code_string)
        # part1 = newAudio[0:t2]
        # part2 = newAudio[t1:]

        exec(code_string+code_string_2)  # string 2 code

        #audio_file.export(output_path, format="mp3")  # Exports to a wav file in the current path.

        print('Done')


def itirate_in_folder(audio_path):
    counter = 1
    for i in os.listdir(audio_path):
        obezlichit(audio_path + '/' + i, f'G:/Python/Markup/Audio_Pull/Obezlichivatel/Final/{counter}.mp3')
        print(f'{counter} done')
        counter += 1
    print('All done')


def make_folder_content_lowercase(folder):
    for i in os.listdir(folder):
        os.rename(folder + '/' + i, folder + '/' + i.lower())



make_folder_content_lowercase('G:/Python/Markup/Audio_Pull/Obezlichivatel/target')
itirate_in_folder('G:/Python/Markup/Audio_Pull/Obezlichivatel/target')
