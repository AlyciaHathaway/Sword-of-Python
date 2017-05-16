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


def print_cluster(raw_data, idx, result):
    print('=' * 50)
    print('第%d个聚类中共有%s份文档,如下:' % (idx + 1, result['num']))
    for doc in result['list']:
        print(raw_data[doc])
    print('-' * 20)
    print('本聚类的中心文档为:')
    print(raw_data[result['_id']])


def main():
    # 读写文件
    df_origin = pd.read_excel(input_path, encoding='utf-8')
    raw_data = list(df_origin.iloc[0:5, 0])
    print(raw_data)
    clusters = nlp.cluster(raw_data)
    print(clusters)
    # lambda
    clusters = sorted(clusters, key=lambda cluster: cluster['num'], reverse=True)
    print(clusters)
    # main中调用打印提取函数，并把idx，cluster作为参数传递
    for idx, cluster in enumerate(clusters):
        print_cluster(raw_data, idx, cluster)

if __name__ == '__main__':
    main()