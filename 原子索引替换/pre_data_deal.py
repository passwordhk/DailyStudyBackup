#!/usr/bin/env python
# encoding: utf-8
# author: huangkai
# file: pre_data_deal.py @time: 2019-03-30 23:36
# contact: 360hkhk@gmail.com

with open('1c.pdb', 'r') as f:
    all_rows_in_list = f.readlines()

results = []
for line in all_rows_in_list:
    data2 = line.split()
    results.append(data2)
for i in results:
#     print(i)# 原子序号替换过程
    if i[-1].startswith('C'):
        i[1] = '1'
    elif i [-1].startswith('H'):
        i[1] = '2'
    elif i[-1].startswith('O'):
        i[1] = '3'
    i.pop() # 删除最后两列
    i.pop()

f2 =open('output.pdb','w')
for i in results:
    # print(i)
    f2.writelines(' '.join(i)+'\n')  # 字符串拼接神器，可以填入一个列表，但元素必须为字符串。
f2.close()

print('Success!')
