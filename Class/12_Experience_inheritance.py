# 继承：子类默认继承父类所有属性和方法

# 1.定义父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# 2.定
class B(A):
    pass


# 3.创建对象验证结论
result = B()
print(result.num)
result.info_print()


