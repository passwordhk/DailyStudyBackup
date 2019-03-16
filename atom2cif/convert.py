#!/usr/bin/env python
# encoding: utf-8
# author: huang-kai
# file: convert.py @time: 2019-03-16 09:49
# contact: 360hkhk@gmail.com
import re
import pandas as pd
import numpy as np

with open('/Users/huangkai/Desktop/dump2clif/sample_data.atom', 'r') as f:
    data_string = f.read()
    # print(data)
    # newdata_string = re.findall('(?<=zs ).*', data_string, re.S)
    newdata_string = re.findall('id.*type.*', data_string, re.S)
    # print(newdata_string[0])

f2 = open('out2pandas.txt', 'w')
f2.write(newdata_string[0])
f2.close()

sheet = pd.read_csv(r'/Users/huangkai/Documents/DailyStudyBackup/atom2cif/out2pandas.txt', sep=' ', engine='python')
df = sheet.dropna(axis=1)
df['type'] = df['type'].apply(
    lambda x: 'C' if x == 1 else ('H' if x == 2 else ('O' if x == 3 else ('Ca' if x == 4 else 'NaN'))))
print(df.head())
atom_count_C = 0
atom_count_H = 0
atom_count_O = 0
atom_count_Ca = 0
arr = []
for index, type1 in zip(df['id'], df['type']):
    #     print(index,type)
    if type1 == 'C':
        atom_count_C += 1
        index = 'C{}'.format(str(atom_count_C))
        arr.append(index)
    elif type1 == 'H':
        atom_count_H += 1
        index = 'H{}'.format(str(atom_count_H))
        arr.append(index)
    elif type1 == 'O':
        atom_count_O += 1
        index = 'O{}'.format(str(atom_count_O))
        arr.append(index)
    elif type1 == 'Ca':
        atom_count_Ca += 1
        index = 'Ca{}'.format(str(atom_count_Ca))
        arr.append(index)
# print(arr)
series_1 = pd.Series(arr)
df['id'] = series_1
# print(df.head())
df['dc_1'] = '0.00000'
df['dc_2'] = 'Uiso'
df['dc_3'] = '1.00'
decimals = pd.Series([5, 5, 5], index=['xs', 'ys', 'zs'])
df.round(decimals)
print(df.head())

df.to_csv('test.csv', header=None, index=None, sep='\t')
