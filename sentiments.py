# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import xlwings as xw

nlp = BosonNLP('siOGjeDh.14548.U8dB4nHYKs-x')

inputPath = r'C:\Main\Desktop\Front End\test\input.xlsx'
outputPath = r'C:\Main\Desktop\Front End\test\output.xlsx'
workBook = xw.Book(inputPath)
sheet = workBook.sheets[1]
sheet.range('A1').value = 'Tags'
sheet.range('B1').value = 'positive'
sheet.range('C1').value = 'negative'
a2 = sheet.range('A2:A73').value

numbers = nlp.sentiment(a2)
positive = []
negative = []

for level1 in numbers:
	positive.append(level1[0])
	negative.append(level1[1])

sheet.range('B2').value = positive[0]
sheet.range('B3').value = positive[1]
sheet.range('B4').value = positive[2]
sheet.range('B5').value = positive[3]

sheet.range('C2').value = negative[0]
sheet.range('C3').value = negative[1]
sheet.range('C4').value = negative[2]
sheet.range('C5').value = negative[3]

workBook.save(outputPath)
# def test(n)
# for key in positive:
# 	n1 = 2
# 	if n1 > 1:
# 		n2 = 'B' + str(n1)
# 	n1 = n1 + 1
# 	print(n1)
# 需要一个闭包
print(a2)
print(numbers)
print(positive)
print(negative)

