import pandas as pd
import collections


'''
This is a scrpit to extract C1_C4 without 'O' from 'fra.out'.
So you must keep the script and 'fra.out' in the same folder
Next,excute this script in Python interpretor and get a datafram
named 'C1_C4_without_O.txt'

'''


# calculate the number of C atoms
def countOfAtoms(formula):
    dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], '', 0, 0
    for c in formula[::-1]:
        if c.isdigit():
            cnt += int(c) * (10 ** i)  # 获取当前数子
            i += 1  # 当前数字的位数
        elif c == ')':  # 当前数字入栈，并更新当前原子的系数
            stack.append(cnt)
            coeff *= cnt
            i = cnt = 0
        elif c == '(':  # 出栈，并更新当前系数（相除哦）
            coeff //= stack.pop()
            i = cnt = 0
        elif c.isupper():  # 原子写入字典，
            elem = c + elem
            dic[elem] += (cnt or 1) * coeff  # 当前数字 * 当前的系数 + 之前已经存在的个数。
            elem = ''
            i = cnt = 0
        elif c.islower():  # 拼接，保留到 elem 中
            elem = c + elem
    for i,j in dic.items():
        if i == 'C':
            return j

# read data from fra.out
df = pd.read_csv('fra.out',sep='\t',engine='python')

col = df.columns.values.tolist()[1:]
if col[-1].startswith('Unname'):
    df.drop(columns=col[-1],inplace=True)
    col = df.columns.values.tolist()[1:]

# get C1_C4 and output
C1_C4 = []
for molecue in col:
    if countOfAtoms(molecue):
        if countOfAtoms(molecue)<=4 and 'O' not in molecue:
            C1_C4.append(molecue)
del_C5More = [i for i in col if i not in C1_C4]
C1_4 = df.drop(columns=del_C5More)
C1_4.to_csv('C1_C4_without_O.txt',index=0)