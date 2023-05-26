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