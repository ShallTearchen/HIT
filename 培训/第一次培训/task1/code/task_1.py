#!/usr/bin/env python
# coding=utf-8

import re

my_dict = dict()

def split_token(token):
    p = "(.*)/(.*)"
    match_obj = re.match(p, token)
    # word = ddmatch_obj.group(1)
    # part_of_speech = match_obj.group(2)
    return match_obj

def insert_dict(word, part_of_speech):
    # print(word, part_of_speech)
    if part_of_speech not in my_dict: 
        my_dict[part_of_speech] = dict()
        my_dict[part_of_speech][word] = 1
    else:
        if word not in my_dict[part_of_speech]:
            my_dict[part_of_speech][word] = 1
        else:
            my_dict[part_of_speech][word] += 1

with open("../corpus/199801_utf.txt", "r") as f:
    for l in f.readlines():
        l = l.strip() # 去掉末尾换行
        if l != "":
            my_list = l.split()
            del my_list[0]
            i = 0
            while i < len(my_list):
                token = my_list[i]
                if token[0] == "[": # 处理带[]的token
                    # 先处理带[的第一部分
                    match_obj = split_token(token[1:])
                    insert_dict(match_obj.group(1), match_obj.group(2))
                    temp = match_obj.group(1)
                    i += 1
                    # 处理中间部分
                    while my_list[i].find("]") == -1:
                        match_obj = split_token(my_list[i])
                        temp += match_obj.group(1)
                        insert_dict(match_obj.group(1), match_obj.group(2))
                        i += 1
                    # 处理最后一部分
                    ind = my_list[i].find("]")
                    match_obj = split_token(my_list[i][:ind])
                    insert_dict(match_obj.group(1), match_obj.group(2))
                    temp += match_obj.group(1)
                    insert_dict(temp, my_list[i][ind + 1:])
                    i += 1
                else: # 处理不带[]的token
                    match_obj = split_token(token)
                    insert_dict(match_obj.group(1), match_obj.group(2))
                    i += 1

with open("./output.txt", "w+") as f:
    f.write(str(my_dict))
    '''
    for key in my_dict.keys():
        f.write("### %s ###" % (key))
        for word in my_dict[key]:
            f.write("%s %s" % (word, my_dict[key][word]))
    '''

# 计算每个类型出现次数最多的前十个
for key in my_dict.keys():
    order_list = sorted(my_dict[key].items(), key = lambda x : x[1], reverse=True)
    print("### %s ###" % key),
    print(order_list[:10])

print("======================================================================================")

# 计算所有类型出现次数最多的前十个
new_dict = dict()
for key in my_dict.keys():
    for word in my_dict[key].keys():
        if word not in new_dict.keys():
            new_dict[word] = my_dict[key][word]
        else:
            new_dict[word] += my_dict[key][word]

order_list = sorted(new_dict.items(), key = lambda x : x[1], reverse=True)
print(order_list[:10])
    
