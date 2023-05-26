# 使用json.dump()来存储数据
import json
numbers = [3, 6, 9, 12, 15, 18]
filename = 'Python_Basics/Read_write_file/numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)