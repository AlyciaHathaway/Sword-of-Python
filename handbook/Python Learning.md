---
title: Python Learning
---
## Python基础
### 输入和输出

 - 输出

	```
	print('Hello, World')
	print('a', 'b', 'c')
	print('1+2')
	```
 - 输入

	```
	name = input('Please enter your name: ')
	Mike
	print('Hello', name)
	```


### 数据类型和变量
#### 数据类型
 - 整数
 - 浮点数
 - 字符串
	- r''表示''内部的字符串默认不转义

		```
		>>> print('\\\t\\')
		\       \
		>>> print(r'\\\t\\')
		\\\t\\
		```

	-  '''...'''的格式表示多行内容

		```
		>>> print('''line1
		... line2
		... line3''')
		line1
		line2
		line3
		```

 - 布尔值
	- 布尔值可以用and、or和not运算
	- 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
 - 空值

#### 变量
#### 常量

 - //地板除，总是得到整数


### 字符串和编码
#### 字符编码
#### 字符串

 - 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符

	```
	>>> ord('A')
	65
	>>> ord('中')
	20013
	>>> chr(66)
	'B'
	>>> chr(25991)
	'文'
	```

 - Python对bytes类型的数据用带b前缀的单引号或双引号表示
 - 以Unicode表示的str通过encode()方法可以编码为指定的bytes

	```
	>>> 'ABC'.encode('ascii')
	b'ABC'
	>>> '中文'.encode('utf-8')
	b'\xe4\xb8\xad\xe6\x96\x87
	>>> '中文'.encode('ascii')
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
	```

 - 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

	```
	>>> b'ABC'.decode('ascii')
	'ABC'
	>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
	'中文
	```

 - 要计算str包含多少个字符，可以用len()函数，len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

 - 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行

	```
	#!/usr/bin/env python3
	# -*- coding: utf-8 -*-
	```

#### 格式化

 - 在Python中，采用的格式化方式和C语言是一致的，用%实现
	```
	>>> 'Hello, %s' % 'world'
	'Hello, world'
	>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
	'Hi, Michael, you have $1000000.'
	```


### list和tuple

#### list

 - list是一种有序的集合，可以随时添加和删除其中的元素

	```
	>>> classmates = ['Michael', 'Bob', 'Tracy']
	>>> classmates
	['Michael', 'Bob', 'Tracy']
	```

 - 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引
 - list是一个可变的有序表，所以，可以往list中追加元素到末尾

	```
	>>> classmates.append('Adam')
	>>> classmates
	['Michael', 'Bob', 'Tracy', 'Adam']
	```

 - 也可以把元素插入到指定的位置，比如索引号为1的位置

	```
	>>> classmates.insert(1, 'Jack')
	>>> classmates
	['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
	```

 - 要删除list末尾的元素，用pop()方法，pop(i)可以传递指定位置参数
 - list里面的元素的数据类型也可以不同

	```
	>>> L = ['Apple', 123, True]
	```

 - list元素也可以是另一个list

	```
	>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
	>>> len(s)
	4
	>>> p = ['asp', 'php']
	>>> s = ['python', 'java', p, 'scheme']
	```

#### tuple

 - tuple一旦初始化就不能修改，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

	```
	>>> classmates = ('Michael', 'Bob', 'Tracy')
	```

 - 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义

	```
	>>> t = (1,)
	>>> t
	(1,)
	```


### 条件判断

 - if else

	```
	age = 3
	if age >= 18:
		print('your age is', age)
		print('adult')
	else:
		print('your age is', age)
		print('teenager')
	```

 - else if

	```
	age = 3
	if age >= 18:
		print('adult')
	elif age >= 6:
		print('teenager')
	else:
		print('kid')
	```

 - 再议 input，因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数

	```
	s = input('birth: ')
	birth = int(s)
	if birth < 2000:
		print('00前')
	else:
		print('00后')
	```


### 循环
#### 循环

 - for...in循环

	```
	names = ['Michael', 'Bob', 'Tracy']
	for name in names:
		print(name)
	```

 - 如果要计算1-100的整数之和，从1写到100有点困难，Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list

	```
	>>> list(range(5))
	[0, 1, 2, 3, 4]
	```

 - while循环，只要条件满足，就不断循环，条件不满足时退出循环

	```
	sum = 0
	n = 99
	while n > 0:
		sum = sum + n
		n = n - 2
	print(sum)
	```

#### break、continue

 - break提前退出循环

	```
	n = 1
	while n <= 100:
		if n > 10: # 当n = 11时，条件满足，执行break语句
			break # break语句会结束当前循环
		print(n)
		n = n + 1
	print('END')
	```

 - continue语句，跳过当前的这次循环，直接开始下一次循环

```
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```


### 使用dict和set
#### dict

 - dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储

```
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
```

 - 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
 - 要避免key不存在的错误
	- 通过in判断key是否存在

	```
	>>> 'Thomas' in d
	False
	```

	- 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value

	```
	>>> d.get('Thomas')
	>>> d.get('Thomas', -1)
	-1
	```

 - dict的key必须是不可变对象，在Python中，字符串、整数等都是不可变的。而list是可变的，就不能作为key。


#### set

 - set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的

	```
	>>> s = set([1, 2, 3])
	>>> s
	{1, 2, 3}
	```

 - 重复元素在set中自动被过滤

	```
	>>> s = set([1, 1, 2, 2, 3, 3])
	>>> s
	{1, 2, 3}
	```

 - 通过add(key)方法可以添加元素到set中
 - 通过remove(key)方法可以删除元素
 - set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

	```
	>>> s1 = set([1, 2, 3])
	>>> s2 = set([2, 3, 4])
	>>> s1 & s2
	{2, 3}
	>>> s1 | s2
	{1, 2, 3, 4}
	```


## 函数
### 调用函数

 - 可以直接从Python的官方网站查看文档http://docs.python.org/3/library/functions.html#abs
 - 也可以在交互式命令行通过help(abs)
 - 调用函数的时候，如果传入的参数数量不对、参数类型不能被函数所接受，会报TypeError的错误
 - 数据类型转换

	```
	>>> int('123')
	123
	>>> int(12.34)
	12
	>>> float('12.34')
	12.34
	>>> str(1.23)
	'1.23'
	>>> str(100)
	'100'
	>>> bool(1)
	True
	>>> bool('')
	False
	```

 - 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

	```
	>>> a = abs # 变量a指向abs函数
	>>> a(-1) # 所以也可以通过a调用abs函数
	1
	```

### 定义函数

 - 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。如果没有return语句，函数执行完毕后也会返回结果，只是结果为None

	```
	def my_abs(x):
		if x >= 0:
			return x
		else:
			return -x
	```

 - 在Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下

 - 如果你已经把`my_abs()`的函数定义保存为`abstest.py`文件了，那么，可以在该文件的当前目录下启动Python解释器，用`from abstest import my_abs`来导入`my_abs()`函数，注意abstest是文件名（不含`.py`扩展名）

#### 空函数

 - 如果想定义一个什么事也不做的空函数，可以用pass语句

	```
	def nop():
		pass
	```

 - pass还可以用在其他语句里

	```
	if age >= 18:
		pass
	```

#### 参数检查

 - 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
 - 如果参数类型不对，Python解释器就无法帮我们检查
 - 修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现

	```
	def my_abs(x):
		if not isinstance(x, (int, float)):
			raise TypeError('bad operand type')
		if x >= 0:
			return x
		else:
			return -x
	```

#### 返回多个值

 - 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标

```
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
```

 - import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数

```
>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print(x, y)
151.96152422706632 70.0
```

 - 但其实这只是一种假象，Python函数返回的仍然是单一值

```
>>> r = move(100, 100, 60, math.pi / 6)
>>> print(r)
(151.96152422706632, 70.0)
```

 - 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便


### 函数的参数
#### 位置参数

 - 对于power(x)函数，参数x就是一个位置参数

	```
	def power(x):
		return x * x
	```

 - 现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数

	```
	def power(x, n):
		s = 1
		while n > 0:
			n = n - 1
			s = s * x
		return s
	```

#### 默认参数

 - 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2

	```
	def power(x, n=2):
		s = 1
		while n > 0:
			n = n - 1
			s = s * x
		return s
	```

 - 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数，需要把参数名写上
 - 定义默认参数要牢记一点：默认参数必须指向不变对象

	```
	def add_end(L=None):
		if L is None:
			L = []
		L.append('END')
		return L
	```

 - 现在，无论调用多少次，都不会有问题

	```
	>>> add_end()
	['END']
	>>> add_end()
	['END']
	```

#### 可变参数

 - 计算a2 + b2 + c2 + ……
	- 普通函数调用的时候，需要先组装出一个list或tuple

	```
	def calc(numbers):
		sum = 0
		for n in numbers:
			sum = sum + n * n
		return sum
	```

	- 如果利用可变参数，可以简化成这样。仅仅在参数前面加了一个`*`号。在函数内部，参数numbers接收到的是一个tuple

	```
	def calc(*numbers):
		sum = 0
		for n in numbers:
			sum = sum + n * n
		return sum
	```

 - 如果已经有一个list或者tuple，要调用一个可变参数怎么办？

	```
	>>> nums = [1, 2, 3]
	>>> calc(*nums)
	14
	```

#### 关键字参数

 - 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

	```
	def person(name, age, **kw):
		print('name:', name, 'age:', age, 'other:', kw)
	```

	- 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数

	```
	>>> person('Michael', 30)
	name: Michael age: 30 other: {}
	```

	- 也可以传入任意个数的关键字参数

	```
	>>> person('Bob', 35, city='Beijing')
	name: Bob age: 35 other: {'city': 'Beijing'}
	>>> person('Adam', 45, gender='M', job='Engineer')
	name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
	```

	- 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

	```
	>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
	>>> person('Jack', 24, **extra)
	name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
	```

#### 命名关键字参数

 - 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数

	```
	def person(name, age, *, city, job):
		print(name, age, city, job)

	>>> person('Jack', 24, city='Beijing', job='Engineer')
	Jack 24 Beijing Engineer
	```

 - 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了

	```
	def person(name, age, *args, city, job):
		print(name, age, args, city, job)
	```

 - 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
 - 命名关键字参数可以有缺省值，从而简化调用

	```
	def person(name, age, *, city='Beijing', job):
		print(name, age, city, job)

	>>> person('Jack', 24, job='Engineer')
	Jack 24 Beijing Engineer
	```

#### 参数组合

 - 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

	```
	def f1(a, b, c=0, *args, **kw):
		print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

	def f2(a, b, c=0, *, d, **kw):
		print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	```

 - 最神奇的是通过一个tuple和dict，你也可以调用上述函数

	```
	>>> args = (1, 2, 3, 4)
	>>> kw = {'d': 99, 'x': '#'}
	>>> f1(*args, **kw)
	a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

	>>> args = (1, 2, 3)
	>>> kw = {'d': 88, 'x': '#'}
	>>> f2(*args, **kw)
	a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
	```

 - 所以，对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的


### 递归函数

 - 我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：`fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n`

	```
	def fact(n):
		if n==1:
			return 1
		return n * fact(n - 1)
	```

 - 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。使用递归函数需要注意防止栈溢出
 - 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的
 - 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

	```
	def fact(n):
		return fact_iter(n, 1)

	def fact_iter(num, product):
		if num == 1:
			return product
		return fact_iter(num - 1, num * product)
	```