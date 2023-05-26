# 在迭代过程中修改输出
file_object = open('Python_Basics/Read_write_file/replace.txt', 'r')
print('File Contentsn' + file_object.read())
file_object.seek(0)

print('nRevised Output')
for line in file_object:
    revised = line.replace('Spanish', 'Mexican')
    print(revised.rstrip())
file_object.close()
