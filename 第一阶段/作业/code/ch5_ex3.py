#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/15 下午10:02
# Author : fred
import os

with open('ch5_3.txt', mode='rt', encoding='utf-8') as read_f,\
    open('ch5_3.txt.swap', mode='wt', encoding='utf-8') as write_f:
    for line in read_f:
        if 'FredXu' in line:
            line = line.replace('FredXu', 'FredXu[fred]')

        write_f.write(line)

os.remove('ch5_3.txt')
os.rename('ch5_3.txt.swap', 'ch5_3.txt')