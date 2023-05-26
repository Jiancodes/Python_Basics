# 返回单个值
def get_full_name(first, last):
    full_name = f'{first} {last}'
    return full_name.title()


comedian = get_full_name('ricky', 'gervais')
print(comedian)