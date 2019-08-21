#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 罗兴红
@contact: EX-LUOXINGHONG001@pingan.com.cn
@file: demo.py
@time: 2019/7/22 15:49
@desc:
'''

s = '''{"error_code":18,"error_msg":"Open api qps request limit reached"}'''
if hasattr(s, 'text'):
    print(s)