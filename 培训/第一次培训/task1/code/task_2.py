#!/usr/bin/env python
# coding=utf-8

import re
import os

def split_token(token):
    p = "(.*)/(.*)"
    match_obj = re.match(p, token)
    return match_obj

os.popen("echo '' > ./train.data")

with open("../corpus/199801_utf.txt", "r") as f:
    for l in f.readlines():
        l = l.strip()
        if l == "":
            continue
        my_list = l.split()
        # 如果训练数据是正向的则可以不需要以下三个列表，直接输出到文件即可
        word_list = list()
        entity_list = list()
        bi_list = list()
        del my_list[0]
        for token in my_list:
            if token[0] == "[":
                match_obj = split_token(token[1:])
            elif token.find("]") != -1:
                ind = token.find("]")
                match_obj = split_token(token[:ind])
            else:
                match_obj = split_token(token)
            word = match_obj.group(1)
            entity = match_obj.group(2)
            for i in range(0, len(word)):
                word_list.append(word[i])
                entity_list.append(entity)
                if i != 0:
                    bi_list.append("I")
                else:
                    bi_list.append("B")
                
        with open("./train.data", "a") as f_2:        
            for i in range(0, len(word_list)):
                # print("%s\t%s\t%s" % (word_list[i], entity_list[i], bi_list[i]))
                f_2.write("%s\t%s\t%s\n" % (word_list[i], entity_list[i], bi_list[i]))

            f_2.write("\n")
        

print("finish")


