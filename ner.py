# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import pandas as pd
import numpy as np
import json
import requests
import asyncio

nlp = BosonNLP('siOGjeDh.14548.U8dB4nHYKs-x')
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
