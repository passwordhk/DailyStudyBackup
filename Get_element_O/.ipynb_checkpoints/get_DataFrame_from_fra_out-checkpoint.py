import pandas as pd
import numpy as np
import re
def out_C_included():
    C_included.to_csv('O_element.out',index=0)
def out_huge_molecue():
    huge.to_csv('huge_molecue.out',index=0)
def out_tiny_molecue():
    tiny_molecue.to_csv('tiny_molecue.out',index=0)
    
    
# 初始化数据    
df = pd.read_csv(r'fra.out',sep='\t',engine='python')
col = df.columns.values.tolist()[1:]
if col[-1].startswith('Unname'):
    df.drop(columns=col[-1],inplace=True)
    col = df.columns.values.tolist()[1:]
# 获取含C分子   
C_list = []
for i in col:
    if i.startswith('C'):
        C_list.append(i)
# 获取C5+分子
huge_molecue = []
for i in C_list:
    if i.startswith('CH') or i.startswith('CO'):
        continue
    if i == 'C':
        continue
    m = re.search(r'(?!C)\d+',i)
    a = m.group(0)
    if int(a)>4:
        huge_molecue.append(i)
# 获取小分子
temp_li = [i for i in col if i not in huge_molecue]
# 获取大分子DataFrame
huge = df.drop(columns=temp_li)
# 获取小分子DataFrame
tiny_molecue = df.drop(columns=huge_molecue)
# 获取含C分子DataFrame
delete_col = []
for i in col[1:]:
    if 'O' not in i:
        delete_col.append(i)
C_included = df.drop(columns=delete_col)
try:
    trigger = input('请输入您需要的导出类型:(输入数字)\n1：含C分子数据表\n2：大分子数据表\n3：小分子数据表\n4：全部\n请输入:')
    if trigger == '1':
        out_C_included()
        print('Done!')
    elif trigger == '2':
        out_huge_molecue()
        print('Done!')
    elif trigger == '3':
        out_tiny_molecue()
        print('Done!')
    elif trigger == '4':
        out_C_included()
        out_huge_molecue()
        out_tiny_molecue()
        print('Done!')
except Exception as e:
    print('请正确输入!')