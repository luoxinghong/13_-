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

logging.basicConfig(level=logging.ERROR,  # 控制台打印的日志级别
                    filename='new.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

headers = {"Content-Type": "application/json"}
url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token=24.6869e85013b17478e8c1977a5a1bc751.2592000.1564207003.282335-16657395"


def try_agin(res):
    if "log_id" in res and "items" in res:
        return False
    else:
        return True


@retry(retry_on_result=try_agin, stop_max_attempt_number=5)
def get_res(data):
    res = requests.post(url, headers=headers, json=data).text
    # 百度智能云词分析接口qps为5，所以设置sleep 0.2
    time.sleep(0.2)
    return res


def run():
    files = os.listdir("./split")
    for file in files:
        data = {}
        f = open("./split/{}".format(file), encoding="utf-8")
        lines = f.readlines()
        count = 1

        for line in lines:
            data["text"] = line.replace("\n", "")
            try:
                res = get_res(data)
                # print(count, line.replace("\n", ""), res)
                with open("./res_split/res_{}".format(file), "a", encoding="utf-8") as g:
                    g.write(str(count) + "" + res + "\n")
                    g.close()
            except Exception as e:
                with open("./res_split/res_{}".format(file), "a", encoding="utf-8") as h:
                    h.write(str(count) + "" + "None" + "\n")
                    h.close()
                logging.error(str(e) + str(file) + str(count) + str(data))
            finally:
                count += 1


if __name__ == "__main__":
    run()
