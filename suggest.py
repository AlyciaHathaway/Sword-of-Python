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
SENTIMENT_URL = 'http://api.bosonnlp.com/suggest/analysis'
headers = {'X-Token': 'siOGjeDh.14548.U8dB4nHYKs-x'}

df_origin = pd.read_excel(input_path, encoding='utf-8')
raw_data = list(df_origin.iloc[0:5, 0])
print(raw_data)

new_array = []
for index, item in enumerate(raw_data):
	resp = requests.post(SENTIMENT_URL, headers=headers, json=item)
	resp = resp.text
	resp_array = json.loads(resp)
	print(resp_array)
	new_array.append(resp_array)

new_data = pd.DataFrame(new_array)
print(new_data)
output = pd.ExcelWriter(output_path)
new_data.to_excel(output, 'sheet1')
output.save()
