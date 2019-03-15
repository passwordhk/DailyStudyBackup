#!/usr/bin/env python
# encoding: utf-8
# author: huang-kai
# file: data2cif.py @time: 2019-03-15 14:03
# contact: 360hkhk@gmail.com

import re
import datetime


def get_timestep_data():
    input_aim = input('请输入您需转换的步长数据，务必仔细核对:')
    start = datetime.datetime.now()
    with open('/Users/huangkai/Desktop/dump2clif/dump4.atom', 'r') as f:
        rows = f.read()

        # print(rows)
        # rule = '{}(.*?)ITEM: T'.format(input_aim)
        rule = '{}.*?(?=ITEM: T)'.format(input_aim)
        aim_text_list = re.findall(rule, rows, re.S)
        aim_text_string = aim_text_list[0]
        # print(aim_text_string)
        # for row in aim_text_string.split('\n'):
        # print(row.strip())
    end = datetime.datetime.now()
    print('该步长数据已获取！耗时%s秒!' % (end - start))
    # for row in rows:r
    #     print(type(row.strip()))
    # col1 = [row.strip() for row in f.read().split('\n') if row.strip()]
    # print(col1)
    return aim_text_string


def create_cif_raw():
    raw_cif = open('output.cif', 'w')
    time = datetime.datetime.now().strftime('%Y-%m-%d')
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


aim_date_block = get_timestep_data()

print(type(aim_date_block))
data = aim_date_block.split('\n')
print(data)
boxsize = []
for index, row in enumerate(data):
    if row.startswith('ITEM: BOX BOUNDS'):
        boxsize.append(data[index + 1].split())
        boxsize.append(data[index + 2].split())
        boxsize.append(data[index + 3].split())
print(boxsize)
box_long = float(boxsize[0][1]) - float(boxsize[0][0])
box_weight = float(boxsize[1][1]) - float(boxsize[1][0])
box_height = float(boxsize[2][1]) - float(boxsize[2][0])
print('计算盒子尺寸成功。。。', box_long, box_weight, box_height)

#     print(type(row))


# def get_case_size():
