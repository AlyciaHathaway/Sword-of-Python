# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import pandas as pd

nlp = BosonNLP('siOGjeDh.14548.U8dB4nHYKs-x')
input_path = r'C:\Main\Desktop\Front End\test\input.xlsx'
output_path = r'C:\Main\Desktop\Front End\test\output.xlsx'


def print_comments(idx, comments):
    print('=' * 50)
    print('第%d组典型意见是:' % (idx + 1))
    print(comments['opinion'])
    print('-' * 20)
    print('共包含%s份文档，意见内容和原文ID如下:' % comments['num'])
    for comment, doc_id in comments['list']:
        print(comment, doc_id)


def main():
    df_origin = pd.read_excel(input_path, encoding='utf-8')
    raw_data = list(df_origin.iloc[0:5, 0])
    print(raw_data)
    all_comments = nlp.comments(raw_data * 2)
    print(all_comments)
    sort_all_comments = sorted(all_comments, key=lambda comments: comments['num'], reverse=True)
    for idx, comments in enumerate(sort_all_comments):
        print_comments(idx, comments)


if __name__ == '__main__':
    main()