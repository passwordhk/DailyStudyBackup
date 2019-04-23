import pandas as pd
import re
df1 = pd.read_csv('O_element.out',sep=',',engine='python')
col_li = df1.columns.values.tolist()
C_li = []
C_filtered = []
for i in col_li[1:]:
    if i.startswith('C'):
        C_li.append(i)
    else:
        C_filtered.append(i)

pattern = re.compile('C(.*?)[A-Z].*?')
C_4 = []
for i in C_li:
    a=re.findall(pattern,i)[0]
    if a == '':
        a = '1'
    if int(a) <= 4:
        C_4.append(i)
# 输出不含C的数据表(原始表为含O成分)
out1 = df1.drop(columns=C_li)
out1.to_csv('不含C的数据表.out',index=0)
# 输出含C的数据表
out2 = df1.drop(columns=C_filtered)
out2.to_csv('含C的数据表.out',index=0)
# 输出含C 小于等于4的数据表
out3 = out2.drop(columns=[i for i in out2.columns.values.tolist()[1:] if i not in C_4])
out3.to_csv('含C且C小于等于4的数据表.out',index=0)