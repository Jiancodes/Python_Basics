# 追加到文件
filename = 'Python_Basics/Read_write_file/anotherfile.txt'
with open(filename, 'a') as file_object:
    file_object.write('Appending this line to the file.n')
    file_object.write('Appending another line to the file.n')