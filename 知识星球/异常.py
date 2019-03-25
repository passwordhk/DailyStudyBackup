'''
编写一个迷你计算器，支持两个数加减乘除
'''
import re
def verify_num(n):
	# 正则判断数字的几种类型
	pattern = re.compile(r'^(-?\d+)(\.\d+)?$')
	return True if re.match(pattern,n) else False
# 老大这种操作，66666~

def verify_opt(opt):
	#判断运算符
	return opt in ['+','-','*','/']

def mini_calculator():
	# 用户输入数据
	user_input = input('Plaese input two numbers and operation,such as 1,2,+:\n')
	try:
		args = user_input.split(',')
		if len(args) == 3:
			a,b,opt = args   # 卧槽，这是什么操作。赋值这么玩
			if not verify_num(str(a)) or not verify_num(str(b)) or not verify_opt(opt):
				print('Input foemat is incorrect!')
				return
			result = eval(f'{a}{opt}{b}')
			print(f'{a}{opt}{b}={result}')
		else:
			print('args\'s length should be 3!')
	except ValueError as e:
		print('Value Error',e)
	except Exception as e:
		print(e)

if __name__ == '__main__':
	mini_calculator()