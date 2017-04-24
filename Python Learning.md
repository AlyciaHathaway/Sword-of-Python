---
title: Python Learning
---
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