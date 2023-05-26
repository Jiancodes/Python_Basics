## 如何在Python中读写文件

Python程序可以从文件中读取信息，也可以向文件中写入数据。虽然普通的旧变量是在程序运行时存储数据的好方法，但如果希望在程序结束后访问该数据，则需要将其保存到文件中。从文件中读取允许您使用范围广泛的信息，而向文件中写入使用户可以在下次运行程序时从他们离开的地方重新开始。您可以从文件中读取数据，将文本写入文件，甚至在数据文件中存储Python结构(如列表)。

### 从文件中读取数据

要从文件中读取，程序需要打开文件，然后读取文件的内容。您可以一次读取文件的全部内容，也可以逐行读取文件。with语句确保在程序完成对文件的访问后正确关闭文件。

### 一次读取整个文件

首先，我们在Python项目的目录中有一个文本文件，以便我们可以使用它。它只是一个简单的文件，用记事本创建，有一些基本的文本。

```python
filename = 'pythonfile.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)
```

关键字是什么?with关键字是一个上下文管理器。它就像一个处理文件的快捷方式，因为它会自动为你打开和关闭文件。例如，如果您需要使用一个文件，则需要打开该文件，并在完成使用后记得关闭它。with open语句为您解决了这个问题。在with上下文中，我们使用open()函数打开文件并返回相应的文件对象。如果无法打开文件，则抛出OSError。使用现在对我们可用的file对象，我们可以使用read()方法读取文件。此方法从文件中返回指定的字节数，默认值为-1，表示读取整个文件。

### 显示文件的属性和模式
```python
filename = 'pythonfile.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print('The filename is: ' + file_object.name)
print('The mode is: ' + file_object.mode)
```

### 逐行读取文件
读取文件的另一种方法是逐行读取。下面是如何做到这一点。
```python
filename = 'pythonfile.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
```
这一次，我们看到了很多额外的空白。为什么呢?这样做的原因是，从文件中读取的每行在行尾都有一个换行符。使用print()函数添加自己的换行符。为了解决这个问题，我们可以使用rstrip()方法在打印到屏幕时删除额外的空白行。
```python
filename = 'pythonfile.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

```
### 在迭代过程中修改输出
在逐行迭代文件以输出时，如果愿意，可以对每次迭代执行操作。这里我们有一个包含以下内容的文本文件。

这段代码将遍历文件的每行，如果找到的话，将“Spanish”替换为“Mexican”。
```python
file_object = open('replace.txt', 'r')
print('File Contentsn' + file_object.read())
file_object.seek(0)

print('nRevised Output')
for line in file_object:
    revised = line.replace('Spanish', 'Mexican')
    print(revised.rstrip())
file_object.close()
```

上面的代码使用了一个我们还没有看到的新方法，seek()方法。seek()方法使用一个指针来跟踪我们在文件中的位置。写和读都会移动寻道指针，如果我们想在多次写入或读取文件后读取该文件，必须将寻道指针设置为零。我们可以通过运行seek()方法或关闭并重新打开代码中的文件来实现这一点。

### 将行存储在列表中
在这段代码中，我们可以看到如何将文件读入列表变量。通过将其打印出来，我们看到文件的内容确实是一个列表。我们还将看到如何遍历列表以打印出文件的内容。

### 写入文件
您可以将'w'参数传递给open()函数，以告诉Python您要写入文件。这将擦除文件中已经存在的任何内容，因此请注意不要覆盖您想要保留的任何数据。
### 创建和写入文件
```python
filename = 'anotherfile.txt'
with open(filename, 'w') as file_object:
    file_object.write('Writing data to a file!')
```

### 将多行写入文件
```python
filename = 'anotherfile.txt'
with open(filename, 'w') as file_object:
    file_object.write('This is line one!n')
    file_object.write('This is line two.n')
```
### 追加到文件
传递'a'参数告诉Python你想要追加到现有文件的末尾。注意，这一次，我们的文件中仍然有上一个示例中的数据。这就是实际的追加行为。
```python
filename = 'anotherfile.txt'
with open(filename, 'a') as file_object:
    file_object.write('Appending this line to the file.n')
    file_object.write('Appending another line to the file.n')
```
### 文件路径
open()函数在正在执行的程序存储的同一目录中查找文件。要从子文件夹打开文件，可以使用相对路径。如果愿意，也可以使用绝对路径。

#### 从子文件夹打开文件
```python
file_path = 'subfolder/valuabledata.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
```
### 使用绝对路径打开文件
```python
file_path = 'C:\Users\MengJian\Desktop\Project\Python_Basics\Read_write_file\valuabledata.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
print(lines)
```
### 使用JSON存储数据

Python有一个JSON模块，允许您将Python数据结构转储到文件中，然后在下次程序运行时从文件中加载该数据。JSON是几乎所有现代编程语言中使用的流行数据格式，因此您可以与可能不使用Python的其他人共享这种数据。在使用数据之前，确保尝试加载的数据存在是很重要的，如果不存在，则应该使用异常处理来管理它。

#### 使用json.dump()来存储数据
```python
import json
numbers = [3, 6, 9, 12, 15, 18]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
```
### 使用json.load()读取数据
```python
import json
filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)
```
### 使用FileNotFoundError管理数据
```python
import json
file_name = 'nonexistent.json'
try:
    with open(file_name) as file_object:
        numbers = json.load(file_object)
except FileNotFoundError:
    message = f'Unable to find file: {file_name}.'
    print(message)
else:
    print(numbers)
```
## 读写不带with关键字的文件
到目前为止的示例显示了在使用with关键字时读取、写入和追加数据。下面是不使用with来执行这些文件操作的方法。

#### 打开一个要写的文件，如果它不存在就创建它
```python
file_object = open('pythonfile.txt', 'w+')
```
#### 打开文件，以便在末尾追加文本



## 用Python使用临时文件

要在Python程序中使用临时文件，可以导入temp_file模块。下面的代码创建了一个临时文件，并将其存储在temp_file变量中。然后，我们可以在临时文件中存储一些数据。在这种情况下，我们把日期定在2020年7月4日，这样我们就不会忘记看烟花了。请注意，我们必须使用小写的b。这是为了将字符串转换为bytes对象，因为这是write()方法在使用tempfile模块时所期望的。现在回想一下，当读取或写入文件时，查找指针被移动。这就是为什么我们在尝试读取临时文件之前将其设置为0的原因。

```python
import tempfile

# Create a temporary file
temp_file = tempfile.TemporaryFile()

# Write to a temporary file
temp_file.write(b'Save the date: 070420')
temp_file.seek(0)

# Read the temporary file
print(temp_file.read())

# Close the temporary file
temp_file.close()

```
## 如何在Python Summary中读写文件

Python提供了处理文件的内置方法。你可以打开文件，写入数据，读取数据，等等。你期望用文件做的所有事情都可以在Python中完成。您不需要导入库来读写文件。使用Python的内置open函数来获取文件对象是处理文件的第一步。这将返回一个我们在本教程的几个示例中看到的文件对象。有几个方法和文件对象的属性可以用来了解您打开的文件。





