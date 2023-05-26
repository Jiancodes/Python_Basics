# 返回字典
def build_house(type, bedrooms):
    house = {'type': type, 'bedrooms': bedrooms}
    return house


house = build_house('Colonial', 3)
print(house)