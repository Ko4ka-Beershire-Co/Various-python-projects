FROM_FOLDER=/mnt/c/Users/Alex/Desktop/share/records/2022/12/02;
TO_FOLDER=/mnt/c/Users/Alex/Desktop/share/text;

readarray -t arr <id_array.txt;
for i in "${arr[@]}";
	do find $FROM_FOLDER -name "${i}" -exec cp "{}" $TO_FOLDER  \;
done
# readarray -t arr <id_array.txt
# for i in "${arr[@]}";
# 	do find /mnt/c/Users/Alex/Desktop/share/records/2022/12/02 -name "${i}" -exec cp "{}" /mnt/c/Users/Alex/Desktop/share/text  \;
# done