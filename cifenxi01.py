#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 罗兴红
@contact: EX-LUOXINGHONG001@pingan.com.cn
@file: demo.py
@time: 2019/5/9 11:04
@desc:
'''
import requests
import time
from retrying import retry
import logging
import os
import grequests
import json


def exception_handler(request, exception):
    print('get response error when at:%s!')


def g_req(data_list):
    headers = {"Content-Type": "application/json"}
    post_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token=24.6869e85013b17478e8c1977a5a1bc751.2592000.1564207003.282335-16657395"
    reqs = (grequests.post(post_url, json=data, headers=headers) for data in data_list)
    res = grequests.map(reqs, exception_handler=exception_handler, size=3)
    return res


def run(file_path, res_path):
    count = 0
    f = open(file_path, "r", encoding="utf-8")

    with open(file_path, mode='r', encoding='utf-8') as f:
        post_data_list = []
        for line in f:
            data = {}
            data["text"] = line.replace("\n", "")
            post_data_list.append(data)
            if len(post_data_list) >= 50:
                reses = g_req(post_data_list)

                for r in reses:
                    if hasattr(r.text, 'text'):
                        count += 1
                        print(count, json.loads(r.text)["text"])
                        with open(res_path, "a", encoding="utf-8") as g:
                            g.write(r.text + "\n")
                            g.close()


if __name__ == "__main__":
    file_path = "./data/segaa"
    res_path = "./res/res_segaa"
    run(file_path, res_path)
