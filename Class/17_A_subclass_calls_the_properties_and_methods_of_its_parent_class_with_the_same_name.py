# 1.师傅类，属性 方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 为了验证多继承，添加了school父类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2.定义徒弟类，继承师傅类 和 学校类 添加父类同名属性和方法
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        # 加自己的初始化的原因: 如果不加这个自己的初始化,kongfu属性值是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名属性和方法，把父类的同名方法和属性再次封装
    def make_master_cake(self):
        # 父类类名.方法()
        # 再次调用初始化的原因，这里想要调用父类的同方方法和属性，属性在__init__初始化位置，所以需要再次调用__init__
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 3.用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

daqiu.make_cake()

daqiu.make_master_cake()
daqiu.make_school_cake()
daqiu.make_cake()

# 结论：如果子类和父类拥有同名属性和方法，子类创建对象和调用属性和方法时，调用到的是子类的同名属性和方法



