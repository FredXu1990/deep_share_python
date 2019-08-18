#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/17 下午8:56
# Author : fred
'''
需求：
用户名，密码和余额存放于文件中，格式为Albert|Alber123|3000
启动程序后：
已注册用户===》先登录===》登录成功===》读取用户余额===》开始购物
    登录过程中，用户密码输入超过3次失败则退出程序
未注册用户===》先注册===>注册成功===》输入用户工资，即为用户余额
===》开始购物，注册过程中，用户密码输入两次一样才可以注册

允许用户根据商品编号购买商品，比如：
1 iPhone
2 macbook
3 bike
用户选择商品后，检测余额是否足够，够就直接扣款，修改文件中的用户余额，不够就提醒
可随时退出，退出时，打印已购买商品和余额
'''
import os

product_list = [
    ['IphoneXR', 9800],
    ['Coffee', 30],
    ['Mac Pro 2019', 25000],
    ["Albert's Python Book", 99],
    ['Bike', 199],
    ['ViVo X20', 2499],
]

shopping_cart = {}
current_user_info = []

db_file = r'db.txt'

while True:
    print('''
    1: Register
    2: Login
    3: Shopping
    ''')

    choice = input('''
    Please choose the function by inputting corresponding number,
    if you input q, you'll quit the program>>:
    ''').strip()

    #user registering
    if choice == '1':
        username = input('please input your username>>:').strip()
        while True:
            password1 = input('please input your password>>:').strip()
            password2 = input('please input your password again>>:').strip()
            if password1 == password2:
                print('register successfully, input 2 to login')
                break
            else:
                print('The twice password are inconsistant.Please input again')

        with open(db_file, 'a', encoding='utf-8') as file:
            file.write('%s|%s\n' % (username, password1))
            file.flush()

    #user logining
    elif choice == '2':
        tag = True
        count = 0
        while tag:
            if count >= 3:
                print("You've failed too many times. You'll quit the program.")
                break

            username = input('username>>:').strip()
            password = input('password>>:').strip()

            #read the user data
            with open(db_file, 'r', encoding='utf-8') as read_f:
                for line in read_f.readlines():
                    print('line')
                    line = line.strip('\n')
                    user_info = line.split('|')

                    username_of_db = user_info[0]
                    password_of_db = user_info[1]

                    #verify user data
                    if username == username_of_db and password == password_of_db:
                        print('Login successfully')
                        if len(user_info) == 3:
                            balance_of_db = user_info[2]
                            balance = int(balance_of_db)
                        else:
                            while True:
                                salary = input('please input your salary>>:').strip()
                                if not salary.isdigit():
                                    continue
                                salary = int(salary)
                                balance = salary
                                break
                        #append the username and balance into the list
                        current_user_info = [username_of_db, balance]
                        print('Hello %s, your balance is %s, input 3 to start shopping' %
                              (current_user_info[0], current_user_info[1]))
                        tag = False
                        break
                    else:
                        print('username or password is invalid')
                        count += 1
                else:
                    print('No user info, please register first')
                    break

            print(current_user_info)


    elif choice == '3':
        if not current_user_info:
            print('Please login first')
        else:
            # get user's balance and then shop
            username_of_db = current_user_info[0]
            balance = current_user_info[1]

            print('Dear user[%s], your balance is [%s], wish you enjoy your shopping' %
                  (username_of_db, balance))
            tag = True
            while tag:
                for index, product in enumerate(product_list):
                    print(index, product)

                choice = input("Input the numbers of product, if you input q, you'll quit the program>>:").strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice< 0 or choice >= len(product_list):
                        print('invalid product number')
                        continue

                    product_name = product_list[choice][0]
                    product_price = product_list[choice][1]

                    if balance > product_price:
                        if product_name in shopping_cart:
                            shopping_cart[product_name]['count'] += 1
                        else:
                            shopping_cart[product_name] = {'product_price':product_price, 'count': 1}

                        balance -= product_price
                        current_user_info[1] = balance
                        print("Added product " + product_name + " into shopping cart, your current "
                                                                "balance " + str(balance))
                    else:
                        print("You can't afford the product. The price of the product is %s, and your're lack"
                              "of %s yuan" % (product_price, product_price - balance))
                        print('your shopping cart is %s' % shopping_cart)

                elif choice == 'q':
                    print("================The goods list you've bought=============")
                    total_cost = 0
                    for i, key in enumerate(shopping_cart):
                        print('%s%23s%23s%23s%23s' % (
                            i,
                            key,
                            shopping_cart[key]['count'],
                            shopping_cart[key]['product_price'],
                            shopping_cart[key]['product_price'] * shopping_cart[key]['count']
                        ))
                        total_cost += shopping_cart[key]['product_price'] * shopping_cart[key]['count']

                    print('''
                    your total expenditure:%s
                    your balance:%s
                    ''' % (total_cost, balance))
                    while tag:
                        inp = input('Confirm purchase(yes/no?)').strip()
                        inp = inp.lower()
                        if inp not in ['y','n','yes','no']:
                            continue
                        if inp in ['y', 'yes']:
                            #write balance into the file
                            src_file = db_file
                            dst_file = r'%s.swap' % db_file
                            with open(src_file, 'r', encoding='utf-8') as read_file,\
                                open(dst_file, 'w', encoding='utf-8') as write_file:
                                for line in read_file:
                                    if line.startswith(username_of_db):
                                        user_info_line_list = line.strip('\n').split('|')
                                        balance_of_db = str(balance)
                                        if len(user_info_line_list) == 2:
                                            user_info_line_list.append(balance_of_db)
                                        else:
                                            user_info_line_list[-1] = balance_of_db
                                        line = '|'.join(user_info_line_list) + '\n'
                                        write_file.write(line)

                            os.remove(src_file)
                            os.rename(dst_file, src_file)
                            print("You've bought successfully. Please wait for the goods patiently")
                            print('log out...')
                            shopping_cart = {}
                            current_user_info = []
                            tag = False
                else:
                    print('Invalid operation')
    elif choice == 'q':
        print('log out...')
        break
    else:
        print('Invalid operation')







