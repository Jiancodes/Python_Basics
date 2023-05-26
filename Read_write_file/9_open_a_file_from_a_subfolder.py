# 从子文件夹打开文件

file_path = 'Python_Basics/Read_write_file/subfolder/valuabledata.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
