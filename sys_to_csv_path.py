import pandas
import os
import sys
import re

# Target_dir = 'C:/Users/Alex/Desktop/WerAndAlignmentCalculator/MARK_NO'

path = input('Путь к sclite.trn.sys, или Enter, если в этой же папке: ')
if path == '':
    __location__ = sys.path[0]
else:
    __location__ = path



with open (str(__location__) + '\\temp.csv', 'w+') as csv:
    csv.write('1,2,3,SPKR,Snt,Wrd,Corr,Sub,Del,Ins,Err,S.Err,\n,,')
    #csv.write('\t')

    with open (str(__location__) + '\\sclite.trn.sys', 'r+', encoding='utf-8') as t:
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

df = pandas.read_csv(str(__location__) + '\\temp.csv')

# Delete first n
df = df.drop(['1','2','3','Unnamed: 12'], axis=1)
df.to_csv(str(__location__) + '\\sclite.csv', index=False)
os.remove(str(__location__) + '\\temp.csv')
