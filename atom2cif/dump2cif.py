#!/usr/bin/env python
# encoding: utf-8
# author: huang-kai
# file: data2cif.py @time: 2019-03-15 14:03
# contact: 360hkhk@gmail.com

import re

input_aim = input('Please input the timestep to convert:')
with open('/Users/huangkai/Desktop/dump2clif/sample_data.atom','r') as f:
    rows = f.read()

    # print(rows)
    # rule = '{}(.*?)ITEM: T'.format(input_aim)
    rule = '{}.*?(?=ITEM: T)'.format(input_aim)
    aim_text_list = re.findall(rule, rows, re.S)
    aim_text_string = aim_text_list[0]
    # print(aim_text_string)
    for row in aim_text_string.split('\n'):
        print(row.strip())
