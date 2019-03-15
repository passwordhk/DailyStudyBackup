li = [i for i in range(1, 21)]
for i in range(len(li)):
    if li[i] % 3 == 0 and li[i] % 5 == 0:
        li[i] = 'appleorange'
    elif li[i] % 3 == 0:
        li[i] = 'apple'
    elif li[i] % 5 == 0:
        li[i] = 'orange'
print(li)