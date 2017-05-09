# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import pandas as pd
import numpy as np
import json
import requests

nlp = BosonNLP('siOGjeDh.14548.U8dB4nHYKs-x')
input_path = r'C:\Main\Desktop\Front End\test\input.xlsx'
output_path = r'C:\Main\Desktop\Front End\test\output.xlsx'
SENTIMENT_URL = 'http://api.bosonnlp.com/ner/analysis'
# 注意：在测试时请更换为您的API Token
headers = {'X-Token': 'siOGjeDh.14548.U8dB4nHYKs-x'}

df = pd.read_excel(input_path, encoding='utf-8')
a = df.iloc[0:3, 0]
print(list(a))
# b = a.to_json(force_ascii=False)
# print(b)

resp = requests.post(SENTIMENT_URL, headers=headers, json = list(a))

resp = resp.text

print(resp)

# dates = pd.date_range('20170501', periods=5)
# print(dates)
# df = pd.DataFrame(resp, index=dates)
# print(df)
#
# writer = pd.ExcelWriter(output_path)
# print(writer)
# df.to_excel(writer, 'sheet1')
# writer.save()

# # mod2_workbook.save(output_path)
