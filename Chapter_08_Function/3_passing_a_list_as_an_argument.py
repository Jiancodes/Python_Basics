# 传递一个列表作为参数

def hello_friends(names):
    for name in names:
        message = f'Hello, {name}!'
        print(message)


hello_friends(['Winnie', 'Mosely', 'Bella', 'Mugsy'])