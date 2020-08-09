# s1 = 'python全栈22期'
# s2 = s1[0]
# print(s2,type(s2))
#对字符串进行索引，切片出来的数据都是字符串类型.
#从左到右都有顺序，下标，索引

#按照索引取值
#
# s3 = s1[2]
# # print(s3)
# s4 = s1[-1]
# print(s4)

#按照切片取值.
# s5 = s1[0:6]
# # print(s5)
# s6 = s1[6:]
# print(s6)

# 切片步长
# s7 = s1[:5:2]
# print(s7)

#倒序:
# s8 = s1[-1:-6:-1]
# print(s8)

#按索引：s1[index]
#按照切片: s1[start_index: end_index+1]
#按照切片步长: s1[start_index: end_index+1:2]
#反向按照切片步长: s1[start_index: end_index后延一位:2]
# #思考题：倒序全部取出?
#
# #练习题:
# a = 'ABCDEFGHIJK' # 从开头取0可以不写
# print(a[0:3])
# print(a[2:5])
# print(a[:]) #默认到最后
# print(a[:-1]) #-1是列表中最后一个元素索引，但是要满足顾头不顾腚原则，所有取不到K元素
# print(a[:5:2]) #加步长
# # print(a[-1:-5:-2]) #反向加步长
#
# #有字符串s = '123a4b5c'
# s = '123a4b5c'
# #通过对s切片形成新的字符串s1, s1 = '123'
# s1 = s[0:3]
# print(s1)
#
# #通过对s切片形成新的字符串s2, s2 = 'a4b'
# s2 = s[3:6]
# print(s2)
# #通过对s切片形成新的字符串s3, s3 = '1345'
# s3 = s[:8:2]
# print(s3)
# #通过对s切片形成字符串s4, s4 = '2ab'
# s4 = s[1:7:2]
# print(s4)
#
# #通过对s切片形成字符串s5, s5 = 'c'
# s5 = s[-1]
# print(s5)
#
# #通过对s切片形成字符串s6, s6 = "ba2"
# s6 = s[-3:-8:-2]
# print(s6)

# #字符串的常用操作方法
s = 'taiBai'
#不会对原字符串进行任何操作，都是产生一个新字符串
# upper lower
# s1 = s.upper()
# s1 = s.lower()
# # print(s1)
#
# #应用
# username = input('用户名')
# password = input('密码')
# code = 'QweA'
# your_code = input('请输入验证码')
# if your_code.upper() == code.upper():
# 	if username == '太白' and password == '123':
# 		print('登录成功')
# 	else:
# 		print('用户名密码错误')
# else:
# 	print('验证码错误')

# print(s.startswith('t'))
# print(s.startswith('taiBai'))
# print(s.startswith('B',3,6))

#replace
msg = 'alex ...'
# msg1 = msg.replace('alex','lm') #默认全部替换
# print(msg1)

# strip:空白：空格, \t \n
# s4 = '	\n太白\t'
#print(s4)
#s5 = s4.strip()
#print(s5)

#了解
# #可以去除指定的字符
# s4 = 'rre太白qsd'
# s5 = s4.strip('reqsd')
# print(s5)

# split 非常重要
# 默认按照空格分隔，返回一个列表
# 指定分隔符
# # str --> list
# s6 = '太白 女神 xx'
# l = s6.split()
# print(l)
# #了解：'
# s6 = ' :太白:女神:wu'
# print(s6.split((':')))
# print(s6.split(':',2))

# join 非常好用
# s1 = 'alex'
# s2 = '+'.join(s1)
# l1 = ['太白','女神','wu']
# #前提：列表里的元素必须都是str类型
# s3 = ':'.join(l1)
# print(s3)

# #count
# s8 = 'aafasaSASDASDAWSASASADA'
# print(s8.count('a'))

#format格式化输出
# 第一种用法:
# msg = '我叫{}今年{}性别{}'.format('大壮',25,'男')
# print((msg))
# 第二种用法
# # msg = '我叫{0}今年{1}性别{2}我依然叫{0}'.format('大壮','25','男')
# # print((msg))
# #第三种用法:
# msg = '我叫{name}今年{age}性别{sex}'.format(age=25,sex='男',name='大壮')
# print((msg))

# is系列
# name = 'taibai123'
# print(name.isalnum()) #字符串由子目或数字组成
# print(name.isalpha()) #字符串只由字母组成
# print(name.isdecimal()) #字符串只由十进制组成
#
# s1 =input('请输入你的金额:')
# if s1.isdecimal():
# 	print((int(s1)))
# else:
# 	print('输入有误')