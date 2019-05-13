import pandas as pd
import collections
df = pd.read_csv('/Users/huangkai/Desktop/fra.out',sep='\t',engine='python')
# 计算碳原子个数
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
# 计算分子量
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

# initialize the data,remove the 'Unmae'!
col = df.columns.values.tolist()[1:]
if col[-1].startswith('Unname'):
    df.drop(columns=col[-1],inplace=True)
    col = df.columns.values.tolist()[1:]
sample_row = df[0:1].values.tolist()[0][1:]
total = 0
for i,j in zip(sample_row,col):
    total += i*cal_mass(j)
    

C36_Max = []
for molecue in col:
    if countOfAtoms(molecue):
        if countOfAtoms(molecue)>=36:
            C36_Max.append(molecue)   

del_col = [i for i in col if i not in C36_Max]
new = df.drop(columns=del_col)
new.to_csv('C36-Max.txt',index=0)

with open('C36-Max.txt') as f:
    content = f.readlines()
    new_col = []
    for i in content:
        new_col.append(i.strip().split(','))
    col_formula = new_col[0][1:]

def massAllAndpercent(li):
#     print(col_formula)
    mass=0
    molecue_count = 0
    for j,k in zip(li[1:],col_formula):
        mass += int(j)*cal_mass(k)
        molecue_count += int(j)
    
    return li[0],molecue_count,mass,mass/total,total
    


with open('C_36ToMaxPercent.txt','w') as f1:
    f1.write('Timestep,molecue_count,C26+Mass,percentage,Mass_total'+'\n')
    for i in new_col[1:]:
        f1.write(''.join(str(massAllAndpercent(i)).strip('()'))+'\n')
        
print('Done!')
    
    