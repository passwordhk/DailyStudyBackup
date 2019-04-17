import re
f = open('1660k.data','r')
all_li = f.readlines()
new = all_li[16:]
content = []
for i in new:
    content.append(i.strip().split())
for i in content:
    if i[1] == '1':
        i[0] = f'C{i[0]}'
    elif i[1] == '2':
        i[0] = f'H{i[0]}'
    elif i[1] == '3':
        i[0] = f'O{i[0]}'
C = []
H = []
O = []
for i in content:
    if i[0].startswith('C'):
        C.append(i[0])
    elif i[0].startswith('H'):
        H.append(i[0])
    elif i[0].startswith('O'):
        O.append(i[0])
# 获取原子固定编号
O_index = [i[1:] for i in O]
C_index = [i[1:] for i in C]
H_index = [i[1:] for i in H]
f.close()

def istype_convert(s):
    a = None
    if s in O_index:
        a = f'O{s}'
    elif s in C_index:
        a = f'C{s}'
    elif s in H_index:
        a = f'H{s}'
    return a

def convert_index(li):
    for i,j in enumerate(li):
        if j=='0':
            b = [0] + [k for k in range(3,i)]
            return b

def get_count_rear(li):
    for index,value in enumerate(li):
        if value == '0':
            return index-3
def cal_mass(formula):
  MM_of_Elements = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067,
                'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305, 'Al': 26.9815386,
                'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078,
                'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
                'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64,
                'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585,
                'Zr': 91.2524, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98.9063, 'Ru': 101.07, 'Rh': 102.9055, 'Pd': 106.42,
                'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.760, 'Te': 127.6,
                'I': 126.90447, 'Xe': 131.2593, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116,
                'Pr': 140.90465, 'Nd': 144.242, 'Pm': 146.9151, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25,
                'Tb': 158.92535, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04,
                'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217,
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
            if Multiply: Multiplier = int(str(Multiplier) + E)
            else: Multiplier = int(E)
            Multiply = True
        elif E.islower(): Element += E
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
        else: Multiplier = int(E)
        Multiply = True
    elif E.islower(): Element += E
    elif E.isupper():
        MM += Multiplier * MM_of_Elements[Element]
        Element, Multiplier, Multiply = E, 1, False
    elif i == len(Compound):
        MM += Multiplier * MM_of_Elements[Element]
        Element, Multiplier, Multiply = E, 1, False
  return MM

f2=open('bonds.reax')
con=f2.readlines()[7:]
a=[]
for i in con:
    a.append(i.strip().split())
    
for i in range(len(a)):
    for j in convert_index(a[i]):
        a[i][j] = istype_convert(a[i][j])

f_temp = open('temp.reax','w')
C_O = []
for i in a:
    f_temp.write('\t'.join(i)+'\n')
f_temp.close()
f2.close()

f3 = open('temp.reax','r')
newcontent = f3.readlines()
f3.close()
# print(newcontent)
C_O_raw = []
for i in newcontent:
    if 'C' in i and 'O' in i:
        C_O_raw.append(i.strip().split())
for i in C_O_raw:
    print(i)
print(len(C_O_raw))

sc = []        
for i in C_O_raw:
#     print(get_count_rear(i))
    if get_count_rear(i) == 1:
        sc.append(i) 
goal = [i for i in C_O_raw if i not in sc]
for i in goal:
    print(i)
print(len(goal))

single = 0
# fuck = 1.039
fuck = 1.037
double = 0
si = []
do = []
for i in goal:
    print(i)
    if i[0][0] =='O':
        if get_count_rear(i) == 2:
            for index,j in enumerate(i):
                if j.startswith('C'):
                    if float(i[index+3])<fuck:
                        print('C-O 单键')
                        single += 1
                        si.append(i[0])
                        si.append(i[index])
                    elif fuck<float(i[index+3])<2:
                        double += 1
                        print('C-O 双键')
                        do.append(i[0])
                        do.append(i[index])
                    elif float(i[index+3])>2:
                        print('C-O 三键')
                      
                        
        elif get_count_rear(i) == 3:
            for index,j in enumerate(i):
                if j.startswith('C'):
                    if float(i[index+4])<fuck:
                        print('C-O 单键')
                        single += 1
                        si.append(i[0])
                        si.append(i[index])
                    elif fuck<float(i[index+4])<2:
                        print('C-O 双键')
                        double += 1
                        do.append(i[0])
                        do.append(i[index])
                    elif float(i[index+4])>2:
                        print('C-O 三键')
        
        elif get_count_rear(i) == 4:
            for index,j in enumerate(i):
                if j.startswith('C'):
                    if float(i[index+5])<fuck:
                        print('C-O 单键')
                        single += 1
                        si.append(i[0])
                        si.append(i[index])
                    elif fuck<float(i[index+5])<2:
                        print('C-O 双键')
                        double += 1
                        do.append(i[0])
                        do.append(i[index])
                    elif float(i[index+5])>2:
                        print('C-O 三键')
                
    elif i[0][0] =='C':
        if get_count_rear(i) == 2:
            for index,j in enumerate(i):
                if j.startswith('O'):
                    if 0<float(i[index+3])<fuck:
                        print('C-O 单键')
                        single += 1
                        si.append(i[0])
                        si.append(i[index])
                    elif fuck<float(i[index+3])<2:
                        print('C-O 双键')
                        double += 1
                        do.append(i[0])
                        do.append(i[index])
                    elif float(i[index+3])>2:
                        print('C-O 三键')
                        
        elif get_count_rear(i) == 3:
            for index,j in enumerate(i):
                if j.startswith('O'):
                    if 0<float(i[index+4])<fuck:
                        print('C-O 单键')
                        single += 1
                        si.append(i[0])
                        si.append(i[index])
                    elif fuck<float(i[index+4])<2:
                        print('C-O 双键')
                        double += 1
                        do.append(i[0])
                        do.append(i[index])
                    elif float(i[index+4])>2:
                        print('C-O 三键')
                        
        elif get_count_rear(i) == 4:
            for index,j in enumerate(i):
                if j.startswith('O'):
                    if float(i[index+5])<fuck:
                        print('C-O 单键')
                        single += 1
                        si.append(i[0])
                        si.append(i[index])
                    elif fuck<float(i[index+5])<2:
                        print('C-O 双键')
                        double += 1
                        do.append(i[0])
                        do.append(i[index])
                    elif float(i[index+5])>2:
                        print('C-O 三键')
print('单键',si)
print('双键',do)
print(f'单键{len(set(si))/2} 双键{len(set(do))/2}')   