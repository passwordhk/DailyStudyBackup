import re

names = (' Kunpen Ji, Li XIAO, Caron Li,'
         ' Dongjian SHI, Ji ZHAO, Fia YUAN Y,'
         ' Wenxue DING, Xiu XU, Haiying WANG, Hai LIN,'
         ' Jey JIANG, Joson WANG E,'
         ' Aiyang ZHANG, Haiying MENG,'
         ' Jack ZHANG E, Chang Zhang, Coron ZHANG')

name_list = names.split(',')
name_list1 = []
for i in name_list:
    name_list1.append(i.strip())
# print(name_list1)

sorted_name_list = sorted(name_list1)
print(sorted_name_list)

Zhang_count = len(re.findall('ZHANG', names, re.IGNORECASE))
print('ZHANG姓氏',Zhang_count, '个人')
def f(x):
    count = 0
    for i in x:
        if i.isalpha():
            count += 1
    return count

length = map(f, sorted_name_list)

for index,name in enumerate(length):
    if name == max(list(length)):
        print(sorted_name_list[index])




