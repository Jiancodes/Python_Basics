# 收集任意数量的关键字参数
def make_a_sandwich(type, **veggies):
    print(f'nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggies[veggie]}')


make_a_sandwich('Ham', one='Onions')
make_a_sandwich('Roast Beef', one='Onions', two='Peppers')
make_a_sandwich('Turkey', one='Olives', two='Spinach', three='Cucumbers')