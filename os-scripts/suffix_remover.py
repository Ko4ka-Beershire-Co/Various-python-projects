import os
import os.path

root_dir = 'C://Users/Alex/Desktop/Folder3'

start = 0
stop = 16 # №-1

while start < stop:

# Counter for 00-15
    if start < 10:
        sub_dir = '0' + str(start)
    elif start >= 10:
        sub_dir = str(start)

    log = str(root_dir) + '/' + str(sub_dir)
    for filename in os.listdir(log):
        os.rename(str(log) + '/'+ str(filename), str(log) + '/' + str(filename[0:15]) + '.ass') # Тут был посос вывожу первые 15

    start = start + 1
    print('Робит нормально---------------'+ str(start) + '/' + str(stop))

# 832899017340209_fd180ac.ass
# 832899017340208_f288febf.ass
