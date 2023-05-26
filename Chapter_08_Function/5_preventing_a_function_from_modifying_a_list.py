# 4.防止函数修改列表
def hello_friends(names):
    while names:
        name = names.pop()
        message = f'Hello, {name}!'
        print(message)


original = ['Winnie', 'Mosely', 'Bella', 'Mugsy']
copy = original[:]
print(original)
hello_friends(copy)
print(original)