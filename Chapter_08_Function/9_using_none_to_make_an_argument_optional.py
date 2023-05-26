# 使用None使参数成为可选的
def describe_car(make, model=None):
    if model:
        print(f'The {make} {model} is a neat vehicle')
    else:
        print(f'The {make} is a neat vehicle')


describe_car('Subaru')
describe_car(model='Corvette', make='Chevy')