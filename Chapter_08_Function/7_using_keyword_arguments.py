# 使用关键字参数
def describe_car(make, model):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru', 'WRX')
describe_car(make='Tesla', model='Model 3')
describe_car(model='Corvette', make='Chevy')