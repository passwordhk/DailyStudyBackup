import re
import csv
import os
import collections
with open('xianglongkai.out') as f:
    raw = f.readlines()
    for_raw = []
    for i in raw:
        if i.startswith('#'):
            i = i[1:]
        for_raw.append(i.strip().split())
    with open('temp.csv','w') as f1:
        for i in for_raw:
            f1.write(','.join(i)+'\n')
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

def get_two_lines(time):
    with open('temp.csv') as f3:
        sample_str = f3.read()
        x = re.search(f'Time.*?\n{time}.*',sample_str).group()
        temp_lines = x.strip().split()
        csv = []
        for i in temp_lines:
            csv.append(i.strip().split(','))

        csv_dict=dict(zip(csv[0],csv[1]))
        return csv_dict
    
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

def parse(csv_dict):
    print('开始分析.......')
    bl = []
    for i in range(5,40):
        bl.append(f'C{i}H')
    C5_39 = []
    key =list(csv_dict.keys())[3:]
#     print(key)
    for i in key:
        if i.startswith('C') and not i.startswith('Ca'):
            if 5<=countOfAtoms(i)<=39:
                C5_39.append(i)
    print('C5-C39:-->',C5_39)
    
    
    less_1 = [i for i in key if i not in C5_39]
    C40_CMax = []
    for i in less_1:
        if i.startswith('C') and not i.startswith('Ca'):
            if countOfAtoms(i) == 40 or countOfAtoms(i)>40:
                C40_CMax.append(i)
    print('C40+:-->',C40_CMax)
    
    
    less_2 = [i for i in less_1 if i not in C40_CMax]
    Ca = []
    for i in less_2:
        if i == 'Ca':
            Ca.append(i)
    print('Ca单质::-->',Ca)
    
    
    less_3 = [i for i in less_2 if i not in Ca]
    inorganic_Ca_complexes = []
    for i in less_3:
        if 'Ca' in i and countOfAtoms(i) == None:
            inorganic_Ca_complexes.append(i)
    print('无机Ca:-->',inorganic_Ca_complexes)
    
    
    others = [i for i in less_3 if i not in inorganic_Ca_complexes]
    print('C1-C4及其他:-->',others)
    
    
    print('总分子种类:',len(others)+len(C5_39) + len(C40_CMax) + len(Ca) + len(inorganic_Ca_complexes),len(key))
    
    # 数据计算阶段
    value0 = 0
    for i in others:
        value0 += cal_mass(i) * int(csv_dict.get(i))
    value1 = 0
    for i in C5_39:
        value1 += cal_mass(i) * int(csv_dict.get(i))
    value2 = 0
    for i in C40_CMax:
        value2 += cal_mass(i) * int(csv_dict.get(i))
    value3 = 0
    for i in Ca:
        value3 += cal_mass(i) * int(csv_dict.get(i))
    value4 = 0
    for i in inorganic_Ca_complexes:
        value4 += cal_mass(i) * int(csv_dict.get(i))

    total = value0 + value1 + value2 + value3

    return [csv_dict.get('Timestep'),str(value0/total),str(value1/total),str(value2/total),str(value3/total),str(value4/total)]

def write_to_file(out):
    with open('result.csv','a+') as res:
        res.write('\t'.join(out)+'\n')
def main():
    a = eval(input('请输入起始步长：'))
    b = eval(input('请输入间隔间距：'))
    c = eval(input('请输入所需数据的组数:'))
    write_to_file(['Timestep','C4_and_others','C5_39','C40_Cmax','Ca','inorganic_Ca_complexes'])
    try:
        for i in range(c):
            content0 = get_two_lines(a)
            res = parse(content0)
            write_to_file(res)
            a += b
    except Exception as e:
        print('溢出')
        os.remove('temp.csv')
if __name__ == '__main__':
  main()