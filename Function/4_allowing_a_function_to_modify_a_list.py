# 允许函数修改列表
def hello_friends(names):
    while names:
        name = names.pop()
        message = f'Hello, {name}!'
        print(message)


original = ['Winnie', 'Mosely', 'Bella', 'Mugsy']
print(original)
hello_friends(original)
print(original)