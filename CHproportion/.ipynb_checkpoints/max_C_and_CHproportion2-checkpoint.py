#!/usr/bin/env python
# encoding: utf-8
# author: huang-kai
# file: max_C_and_CHproportion.py @time: 2019-03-18 21:19
# contact: 360hkhk@gmail.com

import linecache
import os
import re
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''make sure 'species.out' in same directory!!!'''

path = 'species.out'
def cal_mass(formula):
    MM_of_Elements = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107,
                      'N': 14.0067,
                      'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305, 'Al': 26.9815386,
                      'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983,
                      'Ca': 40.078,
                      'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
                      'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723,
                      'Ge': 72.64,
                      'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585,
                      'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98.9063, 'Ru': 101.07, 'Rh': 102.9055,
                      'Pd': 106.42,
                      'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.760, 'Te': 127.6,
                      'I': 126.90447, 'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116,
                      'Pr': 140.90465, 'Nd': 144.242, 'Pm': 146.9151, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25,
                      'Tb': 158.92535, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04,
                      'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23,
                      'Ir': 192.217,
                      'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.9804,
                      'Po': 208.9824, 'At': 209.9871, 'Rn': 222.0176, 'Fr': 223.0197, 'Ra': 226.0254, 'Ac': 227.0278,
                      'Th': 232.03806, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237.0482, 'Pu': 244.0642, 'Am': 243.0614,
                      'Cm': 247.0703, 'Bk': 247.0703, 'Cf': 251.0796, 'Es': 252.0829, 'Fm': 257.0951, 'Md': 258.0951,
                      'No': 259.1009, 'Lr': 262, 'Rf': 267, 'Db': 268, 'Sg': 271, 'Bh': 270, 'Hs': 269, 'Mt': 278,
                      'Ds': 281, 'Rg': 281, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 289, 'Lv': 292, 'Ts': 294, 'Og': 294,
                      'ZERO': 0}

    Compound = formula
    IsPolyatomic, End, Multiply = False, False, False
    PolyatomicMass, MM, Multiplier = 0, 0, 1
    Element = 'ZERO'

    for i in range(0, len(Compound) + 1):
        E = Compound[i:i + 1]
        if IsPolyatomic:
            if End:
                IsPolyatomic = False
                MM += int(E) * PolyatomicMass
            elif E.isdigit():
                if Multiply:
                    Multiplier = int(str(Multiplier) + E)
                else:
                    Multiplier = int(E)
                Multiply = True
            elif E.islower():
                Element += E
            elif E.isupper():
                PolyatomicMass += Multiplier * MM_of_Elements[Element]
                Element, Multiplier, Multiply = E, 1, False
            elif E == ')':
                PolyatomicMass += Multiplier * MM_of_Elements[Element]
                Element, Multiplier = 'ZERO', 1
                End, Multiply = True, False
        elif E == '(':
            MM += Multiplier * MM_of_Elements[Element]
            Element, Multiplier = 'ZERO', 1
            IsPolyatomic, Multiply = True, False
        elif E.isdigit():
            if Multiply:
                Multiplier = int(str(Multiplier) + E)
            else:
                Multiplier = int(E)
            Multiply = True
        elif E.islower():
            Element += E
        elif E.isupper():
            MM += Multiplier * MM_of_Elements[Element]
            Element, Multiplier, Multiply = E, 1, False
        elif i == len(Compound):
            MM += Multiplier * MM_of_Elements[Element]
            Element, Multiplier, Multiply = E, 1, False
    return MM


content = ''
cache_data = linecache.getlines(path)
for line in range(len(cache_data)):
    content += cache_data[line].replace('#', '')
f = open('middle_cache.out', 'w')
f.write(content)
f.close

data = linecache.getlines('middle_cache.out')
# for row in data:
#     print(row.split())
odd_row_raw = data[::2]
even_row_raw = data[1::2]
odd_row = []
even_row = []
for i, j in zip(even_row_raw, odd_row_raw):
    even_row.append(i.strip().split())
    odd_row.append(j.strip().split())

C_H = []
for i in odd_row:
    middle = []
    for j in i:
        if j.startswith('C'):
            #             middle.append(j)
            CnHn = re.sub(r'[O]\d*', '', j)
            middle.append(CnHn)
    C_H.append(middle)

maxxx = []
max_index = []
for i in C_H:
    liii = []

    for index, molecue in enumerate(i):
        liii.append(cal_mass(molecue))
    max_index.append(liii.index(max(liii)))
# print(max_index)

moment = []
for i in even_row:
    moment.append(int(i[0]) / 10000)

formula = []

for i, j in zip(C_H, max_index):
    formula.append(i[j])
# print(formula)

atom_count = []
for i in formula:
    atom_count_element = re.findall('\d+', i)
    atom_count.append(atom_count_element)
# print(atom_count)
C_cout = []
for i in atom_count:
    C_cout.append(int(i[0]))
# print(C_cout)
H_count = []
for i in atom_count:
    H_count.append(int(i[1]))

CHproportion = []
for i, j in zip(C_cout, H_count):
    CHproportion.append(i / j)
HCproportion = []
for i, j in zip(C_cout, H_count):
    HCproportion.append(j / i)
out = list(zip(moment,formula,C_cout,H_count,CHproportion,HCproportion))
f_out = open('out.csv','w')
f_out.write('Timestep,formula,C_cout,H_count,C/H,H/C\n')
for i in out:
	f_out.write(str(i).strip('()')+'\n')
f_out.close()

# print('数据分析完成，正在绘图请耐心等待！')

# print('正在绘制C / ps...')
# sns.stripplot(x=moment, y=C_cout)
# plt.show()
# print('正在绘制C/H...')
# CHproportion = []
# for i, j in zip(C_cout, H_count):
#     CHproportion.append(i / j)
# sns.stripplot(x=moment, y=CHproportion)
# plot.show()

# print('Done!!!')
