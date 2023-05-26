# 1.师傅类，属性 方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2.定义徒弟类，继承师傅类
class Prentice(Master):
    pass

# 3.用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

print(Prentice.__mro__)
