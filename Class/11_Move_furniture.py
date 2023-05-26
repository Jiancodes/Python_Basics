class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return  f'房屋地理位置子在{self.address}, 房屋面积是{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        # 如果家具剩余面积 <= 房屋的剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新
        # 房屋剩余面积 - 该家具的面积
        # 否者：提示用户家具太大，剩余面积不足，无法容纳
        # )
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area = self.free_area - item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')


# 双人床 6
bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)
ball = Furniture('足球场', 2000)

# 房子1 北京  1000
house1 = Home('北京', 1000)

house1.add_furniture(bed)
house1.add_furniture(ball)
print(house1)