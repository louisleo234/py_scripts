#基本结构

'''
while 条件：
    循环体
'''

# while True:
#     print('test')
#     print('不一样')
#     print('a')
#     print('b')
#
# flag = True
# while flag:
#     print('test')
#     print('不一样')
#     flag = False
#     print('a')
#     print('b')

# 1 + 2 + ... 100
# s = 0
# count = 1
# while count < 101:
#     s = s + count
#     count = count + 1
# print(s)

# 偶数100之和
# count = 2
# while True:
#     print(count)
#     count = count + 2
#     if count == 102:
#         break

#方法2:
# count = 1
# while count < 101:
#     if count % 2 == 0:
#         print(count)
#     count = count + 1

#continue 退出本次循环，继续下一次循环
# flag = True
# # while flag:
# #     print(111)
# #     print(222)
# #     flag = False
# #     continue
# #     print(333)

#while else: while循环如果被break打断，则不执行else语句
# count = 1
# while count < 5:
#     print(count)
#     if count == 2:
#         break
#     count = count + 1
# else:
#     print(666)

count = 1
while count <= 3:

    username = input('用户名')
    password = input('密码')
    code = 'qwer'
    your_code = input('验证码: ')
    if your_code == code:
        if username == 'alex' and password == '123':
            print('登录成功')
        else:
            print('用户名密码错误')
    else:
        print('验证码错误')
    count = count + 1
