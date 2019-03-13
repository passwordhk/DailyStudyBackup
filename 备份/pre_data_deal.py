#!/usr/bin/env python
# encoding: utf-8
# author: huangkai
# file: pre_data_deal.py @time: 2019-03-05 23:36
# contact: 360hkhk@gmail.com

with open('1c.pdb', 'r') as f:
    data1 = f.readlines()
    # lines_count = len(f.readlines())
# print('共',lines_count,'行')
results = []
for line in data1:
    data2 = line.split() # 返回分割后的字符串列表,data2为列表类型
    # print(data2)
    results.append(line)

# print(results)

results2 = []
for element in results:       # 拆分两次列表,我也不知道为啥拆两次 *-* 应该是split()把一整行字符串转换为列表
    data3 = element.split()
    results2.append(data3)

for i in results2:      # 原子序号替换过程
    for j in i:
        if 'C' in j:
            i[1] = '1'
        elif 'H' in j:
            i[1] = '2'
        elif 'O' in j:
            i[1] = '3'


f2 =open('output.pdb','w')
for i in results2:
    # print(i)
    f2.writelines(' '.join(i)+'\n')  # 字符串拼接神器
f2.close()
print('Success!')
