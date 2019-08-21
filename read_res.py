#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 罗兴红
@contact: EX-LUOXINGHONG001@pingan.com.cn
@file: demo.py
@time: 2019/7/1 19:25
@desc:
'''
import re

count = 1
f = open("C:/Users/my/Desktop/SPIDER/17_百度智能云/res_split/xxx.txt")
g = open("C:/Users/my/Desktop/SPIDER/17_百度智能云/split/xxx.txt")
line_f = f.readline()
line_g = g.readline()

while line_f:
    if "error_msg" in line_f:
        print(line_f.replace("\n", ""))
    elif re.findall('"text": "items":', line_f)[0] != line_g.replace("\n", ""):
        print(count, re.findall('"text": "items":', line_f)[0])
        print(count, line_g.replace("\n", ""))
    else:
        pass

    line_f = f.readline()
    line_g = g.readline()
    count += 1
