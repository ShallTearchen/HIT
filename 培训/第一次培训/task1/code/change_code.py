#!/usr/bin/env python
# coding=utf-8

import os

def output(path):
    output = os.popen("file -i '{}'".format(path))
    print(output.read())

output("../corpus/199801.txt")

print("changing code...\n")

with open("../corpus/199801.txt", "r", encoding="iso-8859-1") as f_1:
    with open("../corpus/199801_utf.txt", "w") as f_2:
        for l in f_1.readlines(): # 按行读取转换是防止一次读取大文本之后爆内存
            utf_str = l.encode("iso-8859-1").decode("gbk").encode("utf-8").decode("utf-8")
            # print(utf_str)
            f_2.write(utf_str)

output("../corpus/199801_utf.txt")
