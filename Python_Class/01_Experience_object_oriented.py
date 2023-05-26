# 需求：洗衣机 功能：洗衣服
# 1.定义洗衣机类
"""
class 类名()：
    pass
"""

class Washer():
    def wash(self):
        print('能洗衣服')

# 2.创建/实例化对象
# 对象名 = 类名()
haier = Washer()

# 3.验证成果
# 打印haier对象
print(haier)
# 使用wash功能 -- 实例方法/对象方法 -- 对象名.wash()
haier.wash()
