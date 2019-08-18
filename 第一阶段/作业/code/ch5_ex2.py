#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/15 下午10:02
# Author : fred

import sys

list1 = sys.argv #把命令行中解释器后空格分割的所有参数都存成列表

src_file_path = list1[1]
dst_file_path = list1[2]

with open(r'%s' % src_file_path, mode='rb') as src_f,\
     open(r'%s' % dst_file_path, mode='wb') as dst_f:
    for line in src_f:
        dst_f.write(line)