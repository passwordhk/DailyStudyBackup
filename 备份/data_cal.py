#!/usr/bin/env python
# encoding: utf-8
# author: huang-kai
# file: data_cal.py @time: 2019-03-11 21:25
# contact: 360hkhk@gmail.com
import pandas as pd

import linecache

with open('/Users/huangkai/Desktop/分子.csv', 'r') as f:
    molecue = f.readline().split(',')
    mass = f.readline().split(',')
    first_line = linecache.getline('/Users/huangkai/Desktop/分子.csv', 1).strip('\n').split(',')
    second_line = linecache.getline('/Users/huangkai/Desktop/分子.csv', 2).strip('\n').split(',')
    new_col = ['r', 'z', 'u', 'v', 't', 'rou']
    print(first_line)

    # print(molecue)
    for i in range(len(molecue)):
        new_col.append(first_line[i] + '({mass})'.format(mass=second_line[i]))
    # new_col[len(mass)] = 'A3CH2(191)'
f2 = open('output.csv', 'w')
f2.writelines(','.join(new_col))
f2.close()
