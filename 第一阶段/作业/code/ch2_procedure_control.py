#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/14 下午3:02
# Author : fred

'''
1.写一个用户登录认证的程序，比如用户名是‘Albert’，
密码是1，请用户分别输入用户名和密码来认证
'''
name = input('请输入用户名：')
password = input('请输入密码：')

if name == 'Albert' and password == '1':
    print('Albert login success')
else:
    print('用户名或密码错误')


'''
2.写一个打印用户权限的程序，请用户输入用户名来验证

Albert --> 超级管理员
tom  --> 普通管理员
jack,rain --> 业务主管
其他 --> 普通用户

'''
name = input('请输入用户名：')
if name == 'Albert':
    print('超级管理员')
elif name == 'Tom':
    print('普通管理员')
elif name == 'Jack' or name == 'Rain':
    print('业务主管')
else:
    print('普通用户')


'''
3.写一个根据当日日期来说明是否上班的程序，请用户输入日期来获取
'''
today = input('输入日期：')

today = today.lower()

if today in ['saturday','sunday']:
    print('周末愉快，不用上班')
elif today in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print('工作日，正常上班')
else:
    print('''输入日期必须为以下中的一种：
    monday, tuesday, wednesday, thursday, friday，saturday,sunday
    ''')


'''
4.写一个循环验证登录的程序，用户认证登录成功后，输入‘q’退出程序；用户认证失败后重复让用户执行登录操作

'''
name = 'Albert'
password = '1234'

while True:
    input_name = input('请输入用户名：')
    input_pwd = input('密码：')
    if input_name == name and input_pwd == password:
        print('登录成功')
        while True:
            cmd = input('>>(输入quit退出)：')
            if not cmd :
                continue
            if cmd == 'quit':
                print('退出成功')
                break
    else:
        print('用户名或密码错误')
        continue
    break


'''
5.写一个让用户猜年龄的程序，允许用户最多尝试3次；每尝试3次后，如果还没有猜对，就问用户是否还继续玩，如果回答Y或y，就继续让猜3次，以此往复；如果回答N或n，就退出程序；如果猜对了就直接退出

'''
albert_age = 28
log_cnt = 0

while True:
    if log_cnt == 3:
        choice = input('是否继续(Y/N?>>: ')
        if choice.upper() == 'Y':
            log_cnt = 0
        else:
            break

    guess = int(input('age:'))
    if guess == albert_age:
        print('猜对啦')
        break
    else:
        print('猜错啦')
    log_cnt += 1

'''
6.按要求打印如下结果
1）循环输出1 2 3 4 5 6   8 9 10
2）求1-100内所有数的和
3）输出1-100内所有的奇数
4）输出1-100内所有的偶数
5）求1-2+3-4+5...+99的和
'''
'''case1'''
for i in range(1, 11):
    if i == 7:
        continue
    print(i)

'''case2'''
sum = 0
for i in range(1, 101):
    sum += i

print('sum of 1-100: ', sum)

'''case3'''
for cnt in range(1, 101):
    if cnt % 2 != 0:
        print(cnt)


'''case4'''
for cnt in range(1, 101):
    if cnt % 2 == 0:
        print(cnt)

'''case5'''
sum = 0
for cnt in range(1, 100):
    if cnt % 2 != 0:
        sum += cnt
    else:
        sum -= cnt
print('sum of 1-2+3-4+5...+99: ', sum)

'''
7.打印如下金字塔图形，下图为等腰三角形，上面一行永远比下面一行少2颗星且位于下面一行的正上方（两层for循环实现）
#max_level=5
    *        #current_level=1，空格数=4，*号数=1
   ***       #current_level=2,空格数=3,*号数=3
  *****      #current_level=3,空格数=2,*号数=5
 *******     #current_level=4,空格数=1,*号数=7
*********    #current_level=5,空格数=0,*号数=9
'''
max_level = 5
for current_level in range(1, max_level+1):
    print(' '*(max_level - current_level), end='')
    print('*'*(2*current_level - 1))