import re
import sys
from pydub import AudioSegment
import itertools

dictionary = ['Михайловича', 'Компания', "могу услышать", "могу услышать"]

with open('G:/Python/Markup/Audio_Pull/Obezlichivatel/2021-09-13_06-00'
          '-30_resources_79146288865_000of1numo8eb9352grahg5aes1nbvhp.ass', 'r+', encoding='utf-8') as sub:
    body = sub.read()
    # lines to get timings from
    lines = []
    f_lines = []
    for i in dictionary:
        body_processed = re.findall(f'.*?{i}', body, re.MULTILINE)
        print(body_processed[0])
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

    print(f_lines)

    new_list = [2000]

    for k in f_lines:
        for l in k:
            new_list.append(l)
    # Sort
    new_list.sort()

    print(new_list)
    print(len(new_list))

    target_list = []
    count = 0
    while count < len(new_list) - 1:
        timeframe = f'audio_file[{new_list[count]}:{new_list[count + 1]}]+'
        print(timeframe)
        count += 1

        target_list.append(timeframe)

    pre_final = target_list[::2]

    pre_final.append(f'audio_file[{str(new_list[len(new_list) - 1])}:]')

    print(pre_final)

    final = ''

    for n in pre_final:
        final += n

    print(final)

    # Cut file part

    audio_file = AudioSegment.from_mp3("abc.mp3")

    code_string = f'audio_file = {final}'

    # part1 = newAudio[0:t2]
    # part2 = newAudio[t1:]

    exec(code_string)  # string 2 code

    audio_file.export('newaudio_2.mp3', format="mp3")  # Exports to a wav file in the current path.

"""with open('G:/Python/Markup/Audio_Pull/Obezlichivatel/2021-09-13_06-00'
          '-30_resources_79146288865_000of1numo8eb9352grahg5aes1nbvhp.ass', 'r+', encoding='utf-8') as sub:
    body = sub.read()
    body_processed = re.findall(r'Dialogue:(..*?\n)', body, re.MULTILINE)
    print(body_processed)

    with open('G:/Python/Markup/Audio_Pull/Obezlichivatel/2021-09-13_06-00'
              '-30_resources_79146288865_000of1numo8eb9352grahg5aes1nbvhp.txt', 'w+', encoding='utf-8') as t_sub:
        t_sub.writelines(body_processed)"""
