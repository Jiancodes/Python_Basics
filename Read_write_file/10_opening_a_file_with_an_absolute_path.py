# 使用绝对路径打开文件

file_path = 'C:\Users\MengJian\Desktop\Project\Python_Basics\Read_write_file\valuabledata.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
print(lines)