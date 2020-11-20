
import os.path
import shutil

wav_dir = 'C://Users/Alex/Desktop/Folder'
ass_dir = 'C://Users/Alex/Desktop/Folder2'

ass_dir_new = 'C://Users/Alex/Desktop/Folder2/New'

for filename in os.listdir(ass_dir):
    if os.path.isfile(str(ass_dir) + '/' + str(filename)):
        os.remove(str(ass_dir) + '/' + str(filename)[:-4] + '.wav')

        shutil.move(str(ass_dir) + "/" + str(filename), str(ass_dir_new) + "/" + str(filename))
        print(str(filename)[:-4] + '.wav')


for filename in os.listdir(ass_dir_new):
    if filename.endswith(".wav"):
        os.remove(os.path.join(ass_dir_new, filename))
