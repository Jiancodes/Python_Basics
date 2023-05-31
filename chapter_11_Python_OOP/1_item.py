class Item:
    pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))  # Item
print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) # int