## Python函数教程
函数是为完成一项特定工作而设计的命名代码块。函数允许您编写一次代码，然后在需要完成相同任务时运行这些代码。函数可以接收它们需要的信息，并返回它们生成的信息。有效地使用函数使程序更容易编写、阅读、测试和修复。在本教程中，我们将学习如何定义函数、如何传递实参、定义形参、设置默认值等。

### 如何在Python中定义一个函数
要在Python中定义一个函数，可以使用**def**关键字。紧跟在**def**关键字后面的是函数名，其后是一组圆括号()和冒号。函数体缩进一级。根据PEP 8, Python代码的风格指南，缩进级别应该是4个空格。要调用一个函数，只需在函数名后面加上括号()。

#### 定义一个Python函数
```python
def hello_world():
    print('Hello World!')


hello_world()
```
### Python函数实参和形参
当你调用一个函数时，你可以向它传递信息。这就是所谓的论证。在调用函数时，*参数*包含在函数名后面的圆括号中。当您定义一个期望接收一条信息的函数时，它被称为*参数*。函数定义中的圆括号中列出了*参数*。

#### 传递单个参数

```python
def hello_friend(friend):
    print(f'Hello, {friend}!')


hello_friend('Mosely')
hello_friend('Winnie')
```

### 将列表作为参数传递

如果你需要一次传递几个值给一个函数，你可以使用列表来实现。该函数能够处理列表中的值。如果函数对列表进行任何更改，则会修改原始列表。如果需要保持原始列表的完整，可以将列表的副本作为参数传递。

```python
def hello_friends(names):
    for name in names:
        message = f'Hello, {name}!'
        print(message)


hello_friends(['Winnie', 'Mosely', 'Bella', 'Mugsy'])
```

### 允许函数修改列表
下面显示了在函数执行期间如何修改原始列表。该列表开始时有4个名称，但在函数运行后拥有0个名称。
```python
def hello_friends(names):
    while names:
        name = names.pop()
        message = f'Hello, {name}!'
        print(message)


original = ['Winnie', 'Mosely', 'Bella', 'Mugsy']
print(original)
hello_friends(original)
print(original)
```

### 防止函数修改列表
在本例中，我们通过将原始列表的副本传递给函数来确保原始列表保持完整。
```python
def hello_friends(names):
    while names:
        name = names.pop()
        message = f'Hello, {name}!'
        print(message)


original = ['Winnie', 'Mosely', 'Bella', 'Mugsy']
copy = original[:]
print(original)
hello_friends(copy)
print(original)
```

### 位置参数和关键字参数
参数可以是位置的或基于关键字的。位置参数只是将函数调用中的第一个参数与函数定义中的第一个形参对齐，依此类推。关键字实参依赖于程序员在函数调用中指定每个实参应该分配给哪个形参。关键字参数的顺序无关紧要。

#### 使用位置参数

```python
def describe_car(make, model):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru', 'WRX')
describe_car('Tesla', 'Model 3')
describe_car('Tesla', 'Cybertruck')
```
#### 使用关键字参数
```python
def describe_car(make, model):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru', 'WRX')
describe_car(make='Tesla', model='Model 3')
describe_car(model='Corvette', make='Chevy')
```

### 默认值
如果愿意，可以默认指定一个参数。这样，在调用函数时，如果没有提供参数，将使用默认值。具有默认值的形参必须列在函数定义中没有默认值的形参之后，以确保位置实参仍然有效。

#### 使用默认值

```python
def describe_car(make, model='WRX'):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru')
```

#### 使用None使参数成为可选的
```python
def describe_car(make, model=None):
    if model:
        print(f'The {make} {model} is a neat vehicle')
    else:
        print(f'The {make} is a neat vehicle')


describe_car('Subaru')
describe_car(model='Corvette', make='Chevy')
```

### 传递任意数量的参数
如果不知道调用函数时需要多少参数，则可以使用星号*操作符收集任意数量的参数。接受可变数量实参的形参必须出现在函数定义的最后。如果您希望对关键字参数执行此操作，则使用双星号**操作符。这些参数以字典的形式存储，参数名作为键，参数作为值。
```python
def make_a_sandwich(type, *veggies):
    print(f'nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggie}')


make_a_sandwich('Ham', 'Onions')
make_a_sandwich('Roast Beef', 'Lettuce', 'Tomato')
make_a_sandwich('Turkey', 'Lettuce', 'Tomato', 'Peppers')
```

### 收集任意数量的关键字参数
```python
def make_a_sandwich(type, **veggies):
    print(f'nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggies[veggie]}')


make_a_sandwich('Ham', one='Onions')
make_a_sandwich('Roast Beef', one='Onions', two='Peppers')
make_a_sandwich('Turkey', one='Olives', two='Spinach', three='Cucumbers')
```

### 如何构造函数
到目前为止，我们已经看到了一些编写和调用函数的方法。如果您想知道构建代码的最佳方法是什么，请尝试找到一些有效的方法。这是主要目标!有了更多的经验，您将了解是什么使不同的结构(如位置参数和关键字参数)更有优势。只要你的函数在做你想让它们做的工作，那就太好了。

### 返回值
函数做的一项常见工作是返回一个值。换句话说，你想要能够给一个函数一些数据让它给你一些其他的数据或值。为了从函数中获取返回值，调用方应该提供一个可以赋值给返回值的变量。一旦函数到达return语句，它就停止运行。

#### 返回单个值
```python
def get_full_name(first, last):
    full_name = f'{first} {last}'
    return full_name.title()


comedian = get_full_name('ricky', 'gervais')
print(comedian)
```
#### 返回字典
```python
def build_house(type, bedrooms):
    house = {'type': type, 'bedrooms': bedrooms}
    return house


house = build_house('Colonial', 3)
print(house)
```

#### 返回一个带有可选值的字典
```python
def build_house(type, bedrooms, pool=None):
    house = {'type': type, 'bedrooms': bedrooms}
    if pool:
        house['pool'] = pool
    return house


house = build_house('Colonial', 3)
print(house)

house = build_house('Colonial', 2, 'No')
print(house)
```
### 模块
在Python中，函数可以存储在单独的文件中，然后在需要时导入。这就是所谓的模块。模块简化了程序文件。当使用模块时，您将希望将模块文件存储在与主程序相同的目录中。
#### 将函数存储在模块中
**sandwichmaker.py**
```python
def make_a_sandwich(type, *veggies):
    print(f'nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggie}')

```

#### 导入整个模块
**functions.py**

模块中的每个函数都可以在程序文件中使用。
```python
import sandwichmaker

sandwichmaker.make_a_sandwich('Pastrami', 'Lettuce', 'Tomato')
sandwichmaker.make_a_sandwich('Corned Beef', 'Pickles', 'Jalapenos')
```
### 导入具体函数
只有导入的函数在程序文件中可用。
```python
from sandwichmaker import make_a_sandwich

make_a_sandwich('Egg', 'Lettuce', 'Tomato')
make_a_sandwich('Steak', 'Pickles', 'Relish')
```
### 给模块一个别名
```python
import sandwichmaker as s

s.make_a_sandwich('Honey Ham', 'Spinach', 'Tomato')
s.make_a_sandwich('Angus Roast Beef', 'Avacado', 'Sun Dried Tomato')
```
### 给函数一个别名\
```python
from sandwichmaker import make_a_sandwich as mas

mas('Honey Ham', 'Spinach', 'Tomato')
mas('Angus Roast Beef', 'Avacado', 'Sun Dried Tomato')
```
### 从模块中导入所有函数
可以使用通配符导入所有函数，但这可能导致命名冲突，从而导致错误。最好避免这种做法
```python
from sandwichmaker import *

make_a_sandwich('Honey Ham', 'Spinach', 'Tomato')
make_a_sandwich('Angus Roast Beef', 'Avacado', 'Sun Dried Tomato')
```

### Python函数教程总结
所有的编程语言都允许您将需要重用的指令序列捆绑在一起。Python也不例外，它还提供了通过使用这些可重用的功能块来简化程序的能力。函数只是用来完成特定任务的一段代码。函数可以利用传递给它们的数据，并且可以返回各种类型的数据，尽管它们不是必需的。