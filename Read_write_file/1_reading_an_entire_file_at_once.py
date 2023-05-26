filename = 'Python_Basics/Read_write_file/pythonfile.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)
