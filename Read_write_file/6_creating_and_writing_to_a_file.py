# 创建和写入文件
filename = 'Python_Basics/Read_write_file/anotherfile.txt'
with open(filename, 'w') as file_object:
    file_object.write('Writing data to a file!')

