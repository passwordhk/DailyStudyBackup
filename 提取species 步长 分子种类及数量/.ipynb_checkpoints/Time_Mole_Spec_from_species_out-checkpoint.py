f = open('species.out')
new_f = open('Time_Mole_Spec.out','w')
raw = f.readlines()
new = []
new.append(raw[0].strip('# ').split()[0:3])
for i in raw[1:]:
    if not i.startswith('#'):
        new.append(i.strip().split()[0:3])
for i in new[1:]:
    i[0] = str(float(i[0])/10000)
for i in new:
    new_f.write('\t'.join(i)+'\n')
new_f.close()
f.close()