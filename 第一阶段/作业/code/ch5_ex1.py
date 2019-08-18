#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/15 下午10:01
# Author : fred
import os

with open('ch5_1.txt', 'r', encoding='utf-8') as read_f, \
    open('ch5_1.txt.swap', 'w', encoding='utf-8') as write_f:
    s = set()
    for line in read_f:
        if line not in s:
            s.add(line)
            write_f.write(line)

os.remove('ch5_1.txt')
os.rename('ch5_1.txt.swap', 'ch5_1.txt')