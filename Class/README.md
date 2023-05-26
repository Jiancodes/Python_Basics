# Python_Class
## 面向对象编程
面向对象是一种抽象化的编程思想，很多编程语言中都有的一种思想
例如: 洗衣服
思考: 几种途径可以完成洗衣服?
答:手洗和机洗
手洗: 找盆 - 放水 - 加洗粉 - 漫泡 - 搓洗 - 水 - 倒水 - 漂洗N次 - 晾晒
机洗:打开洗衣机 - 放衣服 - 加洗衣粉 - 按下开始按钮 - 晾晒。
思考: 对比两种洗衣服途径，同学们发现了什么?
答:机洗更简单
思考:机洗，只需要找到一台洗衣机，加入简单操作就可以完成洗衣服的工作，而不需要关心洗衣机内
部发生了什么事情。

**总结:面向对象就是将编程当成是一个事物，对外界来说，事物是直接使用的，不用去管他内部的情况。而编程就是设置事物能够做什么事。**
## 二.类和对象
思考: 洗衣机洗衣服描述过程中，洗衣机其实就是一个事物，即对象，洗衣机对象哪来的呢?
答: 洗衣机是由工厂工人制作出来。
思考: 工厂工人怎么制作出的洗衣机?
答:工人根据设计师设计的功能图纸制作洗衣机。
总结: 图纸-洗衣机-洗衣服
在面向对象编程过程中，有两个重要组成部分:类和对象

**类和对象关系：用类去创建（或实例化）一个对象**
### 2.1 理解类和对象
#### 2.1.1类
类是对一系列具有相同特征和行为的事物的统称，是一个抽象的概念不是真实存在的事物。
- 特征即是属性
- 行为即是方法
类比如是制造洗衣机时要用到的图纸，也就是说类是用来创建对象
### 2.2 面向对象实现方法
#### 2.2.1定义类
Python2中类分为: 经典类 和 新式类
- 语法
```python
class 类名():
代码
....
```
** 注意:类名要满足标识符命名规则，同时遵循大驼峰命名习惯**
- 体验
```python
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
```
### 2.2.2 创建对象
对象又名实例
- 语法
```
对象名 = 类名()
```
- 体验
```python
#创建对象
haier1 = Washer()
# <_main__.Washer object at x0000918B7B224240>
print(haier1)
# haier对象调用实例方法
haier1.wash()
```
### 2.2.3 self
self 指的是调用该函数的对象.

## 三.添加和获取对象属性
属性即是特征，比如: 洗衣机的宽度、高度、重量...对象属性既可以在类外面添加和获取，也能在类里面添加和获取
### 3.1 类外面添加对象属性
语法
```python
对象名.属性名 = 值
体验
haier1.width = 50
haier1.height = 809
```
### 3.2 类外面获取对象属性
- 语法
```python
对象名.属性名
```
- 体验
```python
print(f'洗衣机的宽度是 {haier1.width}')
print(f'洗衣机的高度是 {haier1.height}')
```
### 3.3 类里面获取对象属性
- 语法
```python
self.属性名
```
- 体验
```python
class Washer():
    def wash(self):
        print('能洗衣服')

    # 获取对象属性
    def print_info(self):
        # self.属性名
        # print(self.width)
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')
haier1 = Washer()

# 添加属性
haier1.width = 400
haier1.height = 500

# 对象调用方法
haier1.print_info()
```
## 四.魔法方法
在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
### 4.1 __init__()
#### 4.1.1 体验__init__()
思考：洗衣机宽度高度是与身俱来的属性，可不可以在生产过程中就赋予这些属性呢？
答：理应如此
__init__()方法的作用，初始化对象。
```python
class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 400

    def print_info(self):
        print(f'洗衣机的宽度是 {self.width}')
        print(f'洗衣机的高度是 {self.height}')

haier = Washer()   # 创建实例化对象
haier.print_info()
```
注意:
- __init__()方法，在创建一个对象时默认被调用, 不需要手动调用
- __init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去。
#### 4.1.2 带参数的__init__()
思考：一个类可以创建多个对象，如何对不同的对象设置不同的初始化属性呢
答：传参数
```python
class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}, 洗衣机的高度是{self.height}')

haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(100, 200)
haier2.print_info()
```
### 4.2 __str__()
当使用print输出对象的时候，默认打印对象的内存地址。如果类定义了 str 方法，那么就会打印从在这个方法中 return 的数据。
```python
class Washer():
    def __init__(self):
        self.width = 200

    def __str__(self):
        return '解释说明：类的说明或对象状态的说明'

haier = Washer()
print(haier)
```
### 4.3 __del__()
当删除对象时，python解释器也会默认调用_del_()方法。
```python
class Washer():
    def  __init__(self, width, height):
        self.width = width
        self.height = height
    def __del__(self):
        print(f'{self}对象已经被删除')

haier1 = Washer(10，20)

#< main .Washer object at x000026118223278>对象已经被删除
del haier1
```