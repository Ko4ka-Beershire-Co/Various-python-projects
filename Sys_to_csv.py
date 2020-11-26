import pandas
import os
import sys
import re

# Target_dir = 'C:/Users/Alex/Desktop/WerAndAlignmentCalculator/MARK_NO'

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


with open (str(sys.path[0]) + '\\temp.csv', 'w+') as csv:
    csv.write('1,2,3,SPKR,Snt,Wrd,Corr,Sub,Del,Ins,Err,S.Err,\n,,')
    #csv.write('\t')

    with open (str(sys.path[0]) + '\\sclite.trn.sys', 'r+', encoding='utf-8') as t:
        Text = t.readlines()[12:-7]
        count = 0
        for line in Text:
            count += 1 # Ух ты
            if count % 2 == 0:
                i = 0
                #line = re.sub(r'[|](.*)[|]', '', line, re.MULTILINE)
                #csv.write(line)
            else:
                line = re.sub(r'[|](.*)[|](.*)[|](.*)[|]', '\\1\\2\\3', line, re.MULTILINE)
                line = re.sub(r'([^ ]*)( *)', '\\1,', line, 0)
                csv.write(line)

df = pandas.read_csv('temp.csv')

# Delete first n
df = df.drop(['1','2','3','Unnamed: 12'], axis=1)
df.to_csv('sclite.csv', index=False)
#os.remove(str(sys.path[0]) + '\\temp.csv')
