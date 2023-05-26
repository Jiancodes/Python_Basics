# 显示文件的属性和模式

filename = 'Python_Basics/Read_write_file/pythonfile.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print('The filename is: ' + file_object.name)
print('The mode is: ' + file_object.mode)
 
 
