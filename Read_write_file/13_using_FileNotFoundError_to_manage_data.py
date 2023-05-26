# 使用FileNotFoundError管理数据
import json
file_name = 'nonexistent.json'
try:
    with open(file_name) as file_object:
        numbers = json.load(file_object)
except FileNotFoundError:
    message = f'Unable to find file: {file_name}.'
    print(message)
else:
    print(numbers)