# 使用json.load()读取数据

import json
filename = 'Python_Basics/Read_write_file/numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)