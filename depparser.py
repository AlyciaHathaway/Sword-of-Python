# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import xlwings as xw
import xlrd

nlp = BosonNLP('siOGjeDh.14548.U8dB4nHYKs-x')
inputPath = r'C:\Main\Desktop\Front End\test\input.xlsx'
outputPath = r'C:\Main\Desktop\Front End\test\output.xlsx'

# xlrd模块
# 计算表格总行数
mod1Data = xlrd.open_workbook(inputPath)
mod1Table = mod1Data.sheets()[0]
mod1Nrows = mod1Table.nrows
mod1NrowsStr = str(mod1Table.nrows)
# print(mod1Nrows)

# xliwngs模块
mod2Workbook = xw.Book(inputPath)
mod2Table = mod2Workbook.sheets[0]
# 头部
mod2Table.range('A1').value = 'text'
mod2Table.range('B1').value = 'head'
mod2Table.range('C1').value = 'role'
mod2Table.range('D1').value = 'tag'
mod2Table.range('E1').value = 'word'

# 获取rawData范围
rawData = mod2Table.range('A2:A' + mod1NrowsStr).value
# 传给波森，并把返回的数据push到情感数组里
data = nlp.depparser(rawData)
print(data)

for index,item in enumerate(data):
	print(index, item)
	head = ','.join(data[index]['role'])
	mod2Table.range('C' + str(index + 2)).value = head
	head = ','.join(data[index]['tag'])
	mod2Table.range('D' + str(index + 2)).value = head
	head = ','.join(data[index]['word'])
	mod2Table.range('E' + str(index + 2)).value = head
	# for i in range(4):
	# 	print(i)
	# 	s = item[i]['head']
	# 	print(s)

mod2Workbook.save(outputPath)
