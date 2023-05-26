# 1.定义一个Python函数

def hello_world():
    print('Hello World')


hello_world()

# 2.传递单个参数

def hello_friend(friend):
    print(f'Hello, {friend}!')


hello_friend('Mosely')
hello_friend('Winnie')

# 3.允许函数修改列表

def hello_friends(names):
    while names:
        name = names.pop()
        message = f'Hello, {name}!'
        print(message)


original = ['Winnie', 'Mosely', 'Bella', 'Mugsy']
print(original)
hello_friends(original)
print(original)

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

# 5.位置参数和关键字参数
def describe_car(make, model):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru', 'WRX')
describe_car('Tesla', 'Model 3')
describe_car('Tesla', 'Cybertruck')

# 6.使用关键字参数
def describe_car(make, model):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru', 'WRX')
describe_car(make='Tesla', model='Model 3')
describe_car(model='Corvette', make='Chevy')

# 7.使用默认值
def describe_car(make, model='WRX'):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru')

# 使用None使参数成为可选的
def describe_car(make, model=None):
    if model:
        print(f'The {make} {model} is a neat vehicle')
    else:
        print(f'The {make} is a neat vehicle')


describe_car('Subaru')
describe_car(model='Corvette', make='Chevy')

# 传递任意数量的参数
def make_a_sandwich(type, *veggies):
    print(f'nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggie}')


make_a_sandwich('Ham', 'Onions')
make_a_sandwich('Roast Beef', 'Lettuce', 'Tomato')
make_a_sandwich('Turkey', 'Lettuce', 'Tomato', 'Peppers')

# 收集任意数量的关键字参数
def make_a_sandwich(type, **veggies):
    print(f'nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggies[veggie]}')


make_a_sandwich('Ham', one='Onions')
make_a_sandwich('Roast Beef', one='Onions', two='Peppers')
make_a_sandwich('Turkey', one='Olives', two='Spinach', three='Cucumbers')

# 返回单个值
def get_full_name(first, last):
    full_name = f'{first} {last}'
    return full_name.title()


comedian = get_full_name('ricky', 'gervais')
print(comedian)

# 返回字典
def build_house(type, bedrooms):
    house = {'type': type, 'bedrooms': bedrooms}
    return house


house = build_house('Colonial', 3)
print(house)

# 返回一个带有可选值的字典
def build_house(type, bedrooms, pool=None):
    house = {'type': type, 'bedrooms': bedrooms}
    if pool:
        house['pool'] = pool
    return house


house = build_house('Colonial', 3)
print(house)

house = build_house('Colonial', 2, 'No')
print(house)

