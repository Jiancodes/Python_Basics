# 逐行读取文件
filename = 'Python_Basics/Read_write_file/pythonfile.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

    
