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
SENTIMENT_URL = 'http://api.bosonnlp.com/tag/analysis'

headers = {'X-Token': 'siOGjeDh.14548.U8dB4nHYKs-x'}

df_origin = pd.read_excel(input_path, encoding='utf-8')
raw_data = list(df_origin.iloc[0:5, 0])
print(raw_data)


async def response():
	resp = requests.post(SENTIMENT_URL, headers=headers, json=raw_data)
	resp = resp.text
	resp_array = json.loads(resp)
	print(resp_array)
	await asyncio.sleep(2)
	new_data = pd.DataFrame(resp_array)

	print(new_data)

	output = pd.ExcelWriter(output_path)
	new_data.to_excel(output, 'sheet1')
	output.save()
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(response())
loop.close()