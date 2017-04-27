# -*- coding: utf-8 -*-
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
mod1Table = mod1Data.sheets()[1]
mod1Nrows = mod1Table.nrows
mod1NrowsStr = str(mod1Table.nrows)
# print(mod1Nrows)

# xliwngs模块
mod2Workbook = xw.Book(inputPath)
# 头部
mode2Table = mod2Workbook.sheets[1]
mode2Table.range('A1').value = 'Tags'
mode2Table.range('B1').value = 'positive'
mode2Table.range('C1').value = 'negative'
# 获取rawData范围
rawData = mode2Table.range('A2:A' + mod1NrowsStr).value
# 传给波森，并把返回的数据push到情感数组里
data = nlp.sentiment(rawData)
positive = []
negative = []

for level1 in data:
	if level1[0] > 0.5:
		positive.append(level1[0])
	else:
		positive.append(level1[1])
	if level1[1] < 0.5:
		negative.append(level1[1])
	else:
		negative.append(level1[0])


# print(positive)
# def test():
# 迭代情感数组和下标，并依次写入新的文件
for index,item in enumerate(positive):
	# print(index)
	# print(item)
	mode2Table.range('B' + str(index+2)).value = item

for index,item in enumerate(negative):
	# print(index)
	# print(item)
	mode2Table.range('C' + str(index+2)).value = item

mod2Workbook.save(outputPath)
# 需要一个闭包
# print(rawData)
# print(data)
# print(positive)
# print(negative)

