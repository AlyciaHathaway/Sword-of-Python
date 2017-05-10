# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import pandas as pd
import numpy as np
import json
import requests
import asyncio

nlp = BosonNLP('siOGjeDh.14548.U8dB4nHYKs-x')
<<<<<<< HEAD
inputPath = r'C:\Main\Desktop\Front End\test\input.xlsx'
outputPath = r'C:\Main\Desktop\Front End\test\output.xlsx'


# xlrd模块aaaaa
# 计算表格总行数
mod1Data = xlrd.open_workbook(inputPath)
mod1Table = mod1Data.sheets()[0]
mod1Nrows = mod1Table.nrows
mod1NrowsStr = str(mod1Table.nrows)

# xliwngs模块
mod2Workbook = xw.Book(inputPath)
mod2Table = mod2Workbook.sheets[0]
# 头部
mod2Table.range('A1').value = 'text'
mod2Table.range('B1').value = 'tag'
mod2Table.range('C1').value = 'word'
mod2Table.range('D1').value = 'entity'
# 获取rawData范围
rawData = mod2Table.range('A2:A' + mod1NrowsStr).value
# 传给波森，并把返回的数据push到数组里
data = nlp.ner(rawData)
# print(data)
tag = []
word = []
entity = []

for index,json in enumerate(data):
	tag.append(data[index]['tag'])
	word.append(data[index]['word'])
	entity.append(data[index]['entity'])
print(tag)
print(word)
print(entity)

for index,item in enumerate(tag):
	itemConcat = ','.join(item)
	mod2Table.range('B' + str(index + 2)).value = itemConcat

for index, item in enumerate(word):
	itemConcat = ','.join(item)
	mod2Table.range('C' + str(index + 2)).value = itemConcat

for index, item in enumerate(entity):
	# print(index, item)
	for index2, item2 in enumerate(item):
		# print(index2, item2)
		for index3, item3 in enumerate(item2):
			pass
			# print(index3, item3)
			print(item[index3][2])
		# print(itemConcat)
	# print(itemConcat)
	# mod2Table.range('D' + str(index + 2)).value = itemConcat

# mod2Workbook.save(outputPath)
=======
input_path = r'C:\Main\Desktop\Front End\test\input.xlsx'
output_path = r'C:\Main\Desktop\Front End\test\output.xlsx'
SENTIMENT_URL = 'http://api.bosonnlp.com/ner/analysis'

headers = {'X-Token': 'siOGjeDh.14548.U8dB4nHYKs-x'}

df = pd.read_excel(input_path, encoding='utf-8')
raw_data = list(df.iloc[0:5, 0])
print(raw_data)
# b = a.to_json(force_ascii=False)
# print(b)

async def response():
	resp = requests.post(SENTIMENT_URL, headers=headers, json=raw_data)
	resp = resp.text
	print(resp)
	print(type(json.loads(resp)))
	resp_array = json.loads(resp)
	dates = pd.date_range('20170501', periods=5)
	await asyncio.sleep(2)
	# 不是异步的问题，是不是本地应该写入到一个文件的问题？但不是赋值给了resp吗
	# 打断点调试
	# 波森传回来的resp是一个字符串数组'[]'，无语。。。
	# 想杀了后端的心都有，接口数据定义的这么混乱
	# 为什么昨天上午用xlwings库时传来的数据能用
	# json序列化解决
	new_data = pd.DataFrame(resp_array, index=dates)

	print(new_data)

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(response())
loop.close()



# writer = pd.ExcelWriter(output_path)
# print(writer)
# df.to_excel(writer, 'sheet1')
# writer.save()
<<<<<<< HEAD

# # mod2_workbook.save(output_path)
>>>>>>> refs/remotes/origin/master
=======
>>>>>>> refs/remotes/origin/master
