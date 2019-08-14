#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/5 下午10:14
# Author : fred


age = 28
user_guess_age = int(input("请输入猜的年龄："))
while True:

    if user_guess_age < age:
        print("再大一点")
        user_guess_age = int(input("请输入猜的年龄："))
    elif user_guess_age > age:
        print("再小一点")
        user_guess_age = int(input("请输入猜的年龄："))
    else:
        print("恭喜你，猜中了")
        break

print('游戏结束')
