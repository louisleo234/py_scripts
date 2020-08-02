# msg = '''___________  info of %s  _______________
# name : 李明
# Age : 18
# job : IT
# Hobby : 运动
# ___________ end _____________'''

# 制作一个公共的模板
# 让一个字符串的某些位置变成动态可传入的

#格式化输出
name = input('请输入你的姓名')
age = input('请输入你的年龄')
job = input('请输入你的工作')
hobby = input('请输入你的爱好')

# %占位符 s --> str
msg = '''___________  info of %s  _______________
name : %s
Age : %s
job : %s
Hobby : %s
___________ end _____________''' % (name,name,age,job,hobby)
print(msg)

