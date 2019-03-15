import random
import string

character = string.ascii_letters
number = string.digits
material = number + character
for i in range(200):
    active_code = ''.join(random.sample(material, 20))
    if active_code.isalnum():
        print('Active_Code:%s' % i, active_code)
# >>> (1-10/62)**20
# 0.029664230203186162  还是有近3%的概率会出现一个数字都不出现的情况
