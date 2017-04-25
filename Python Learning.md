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
**数据类型**
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

**变量**
**常量**

 - //地板除，总是得到整数


### 字符串和编码
**字符编码**
**字符串**

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

**格式化**

 - 在Python中，采用的格式化方式和C语言是一致的，用%实现
	```
	>>> 'Hello, %s' % 'world'
	'Hello, world'
	>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
	'Hi, Michael, you have $1000000.'
	```


### list和tuple

**list**

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

**tuple**

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
**循环**

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

**break、continue**

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
**dict**

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


**set**

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

