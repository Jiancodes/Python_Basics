# 具有任意数量参数的函数
def make_a_sandwich(type, *veggies):
    print(f'nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggie}')


make_a_sandwich('Ham', 'Onions')
make_a_sandwich('Roast Beef', 'Lettuce', 'Tomato')
make_a_sandwich('Turkey', 'Lettuce', 'Tomato', 'Peppers')
