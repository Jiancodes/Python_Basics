# 将行存储在列表中
filename = 'Python_Basics/Read_write_file/pythonfile.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.rstrip())
