#!/usr/bin/env python
# encoding: utf-8
# author: huang-kai
# file: data2cif.py @time: 2019-03-15 14:03
# contact: 360hkhk@gmail.com

import re
import datetime
import pandas as pd
import numpy as np

def get_timestep_data():
    print('请确保使用前将dump文件命名为dump.atom且与此脚本同目录！！！', end='')
    input_aim = input('请输入您需转换的步长数据，并仔细核对:')
    with open('dump4.atom', 'r') as f:
        rows = f.read()
        # print(rows)
        # rule = '{}(.*?)ITEM: T'.format(input_aim)
        rule = '{}.*?(?=ITEM: T)'.format(input_aim)
        aim_text_list = re.findall(rule, rows, re.S)
        global aim_text_string
        aim_text_string = aim_text_list[0]
        # print(aim_text_string)
        # for row in aim_text_string.split('\n'):
        # print(row.strip())
    # end = datetime.datetime.now()
    # for row in rows:r
    #     print(type(row.strip()))
    # col1 = [row.strip() for row in f.read().split('\n') if row.strip()]
    # print(col1)
    f_aim_text=open('aim_middle.atom', 'w')
    f_aim_text.write(aim_text_string)
    f_aim_text.close()
    print('以获取目标数据块...')

def create_cif_raw():
    raw_cif = open('output.cif', 'w')
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    aim_date_block = aim_text_string
    global start
    start = datetime.datetime.now()
    # print(type(aim_date_block))
    data = aim_date_block.split('\n')
    # print(data)
    boxsize = []
    for index, row in enumerate(data):
        if row.startswith('ITEM: BOX BOUNDS'):
            boxsize.append(data[index + 1].split())
            boxsize.append(data[index + 2].split())
            boxsize.append(data[index + 3].split())
    # print(boxsize)
    box_long = float(boxsize[0][1]) - float(boxsize[0][0])
    box_weight = float(boxsize[1][1]) - float(boxsize[1][0])
    box_height = float(boxsize[2][1]) - float(boxsize[2][0])
    print('计算盒子尺寸成功...', box_long, box_weight, box_height)
    header_text = '''data_reax2ms
_audit_creation_date	{}
_audit_creation_method	'Materials Studio'
_symmetry_space_group_name_H-M	'P1'
_symmetry_Int_Tables_number	1
_symmetry_cell_setting	triclinic
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
_cell_length_a	{}
_cell_length_b	{}
_cell_length_c	{}
_cell_angle_alpha	90.0000
_cell_angle_beta	90.0000
_cell_angle_gamma	90.0000
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy'''.format(time, box_long, box_weight, box_height)

    raw_cif.write(header_text)
    raw_cif.close()
    print('初始化cif成功...')


def convert2cif():
    with open('aim_middle.atom', 'r') as f:
        data_string = f.read()
        # print(data)
        # newdata_string = re.findall('(?<=zs ).*', data_string, re.S)
        newdata_string = re.findall('id.*type.*', data_string, re.S)
        # print(newdata_string[0])

    f2 = open('out2pandas.txt', 'w')
    f2.write(newdata_string[0])
    f2.close()

    sheet = pd.read_csv('out2pandas.txt', sep=' ', engine='python')
    df = sheet.dropna(axis=1)
    df['type'] = df['type'].apply(
        lambda x: 'C' if x == 1 else ('H' if x == 2 else ('O' if x == 3 else ('Ca' if x == 4 else 'NaN'))))
    # print(df.info())
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
    # decimals = pd.Series([6, 6, 6], index=['xs', 'ys', 'zs'])
    # df.round(decimals)
    # print(df.head())

    body_cif = df.to_csv('body.cif', float_format='%.6f', header=None, index=None, sep='\t', encoding='utf-8')
    f3 = open('body.cif', 'r')
    wrinte_in =f3.read()
    f3.close()
    final = open('output.cif', 'a+')
    final.write('\n'+ wrinte_in)
    final.close()

if __name__ == '__main__':
    get_timestep_data()
    create_cif_raw()
    convert2cif()
    end = datetime.datetime.now()
    print('转换成功，耗时{}秒...\n已在此目录下生成output.cif目标文件！！！'.format(end-start))