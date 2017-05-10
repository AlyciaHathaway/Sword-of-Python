---
title: Pandas库（一）
---
### Series
```
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print(s.index)
```
### DataFrame
**创建一个DataFrame，包括一个numpy array, 时间索引和列名字**
```
dates = pd.date_range('20170508', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
```
**查看数据**
```
print(df.head())
print(df.tail())
print(df.index)
print(df.columns)
print(df.values)
# 使用 describe() 函数对于数据的快速统计汇总
print(df.describe())
print(df.T)
print(df.sort_values(by='A'))
```
**选择数据**
```
# 选择一列数据
print(df.A)
print(df['A'])
# 选择多列数据
print(df[['A', 'B']])
# 选择多行数据
print(df[0:3])
# 按 index 选取多行
print(df['2017-05-08':'2017-05-09'])
```
**使用标签选取数据**
```
# df.loc[行标签,列标签]
print(df.loc['2017-05-08':'2017-05-09'])    # 选择前两行数据
print(df.loc[:, 'A':'B'])   # 选择AB两列数据
```
**使用位置选取数据**
```
# df.iloc[行位置,列位置] PS：iloc 则为 integer & location 的缩写
print(df.iloc[1, 1])    # 选取第二行，第二列的值，返回的为单个值
print(df.iloc[[0, 2], :])    # 选取第一行及第三行的数据
print(df.iloc[0:2, :])  # 选取第一行到第三行（不包含）的数据
print(df.iloc[:, 1])    # 选取所有记录的第二列的值，返回的为一个Series
print(df.iloc[1, :])    # 选取第一行数据，返回的为一个Series
```
**更广义的切片方式是使用.ix，它自动根据给到的索引类型判断是使用位置还是标签进行切片**
```
print(df.ix[0, 0])
print(df.ix['2017-05-08', 'A'])
```
**通过逻辑指针进行数据切片**
```
# df[逻辑条件]
print(df[df.A > 1])
print(df[(df.A > 0.1) & (df.A < 1)])
# 使用isin()方法来过滤在指定列中的数据
print(df[df['A'].isin([1, 9])])    # 选取A列中数为1和9的数
```
