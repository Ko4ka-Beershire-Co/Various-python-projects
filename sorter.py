import os
import os.path
import shutil

wav_dir = 'C://Users/Alex/Desktop/Folder3'
ass_dir = 'C://Users/Alex/Desktop/Folder2'

ass_dir_new = 'C://Users/Alex/Desktop/Folder2/New'

start = 0
stop = 16 # №-1

while start < stop:

# Counter for 00-15
    if start < 10:
        sub_dir = '0' + str(start)
    elif start >= 10:
        sub_dir = str(start)

# Create folder %loop_value% [the way big boys do, with Er handling and a notification]
    loop_dir = str(ass_dir_new) + '/' + str(sub_dir)
    try:
        os.mkdir(loop_dir)
    except OSError:
        print ("Все сломалось, ничего не робитъ")
    else:
        print('Робит нормально---------------'+ str(start) + '/' + str(stop))

# Move .wav to target
    source_dir = str(wav_dir) + '/' + str(sub_dir)
    wav = os.listdir(source_dir)
    for filename in wav:
        shutil.move(os.path.join(source_dir, filename), ass_dir)

# Match, move
    for filename in os.listdir(ass_dir):
        if os.path.isfile(str(ass_dir) + '/' + str(filename)[:-13] + '.wav'):
            os.remove(str(ass_dir) + '/' + str(filename)[:-13] + '.wav')
            new_dir = str(ass_dir_new) + '/' + str(sub_dir)
            shutil.move(str(ass_dir) + "/" + str(filename), str(new_dir) + '/' + str(filename))
            print(str(filename)[:-13] + '.wav')

# Remove
    for filename in os.listdir(ass_dir_new):
        if filename.endswith(".wav"):
            os.remove(os.path.join(ass_dir_new, filename))
# Loop next
    start = start + 1
