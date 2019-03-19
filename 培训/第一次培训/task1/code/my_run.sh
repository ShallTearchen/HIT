#!/bin/bash

# 训练数据
crf_learn template train.data model 
# 测试数据
crf_test -m model train.data > output.txt
# 评估效果
perl conlleval.pl -d "\t" < output.txt
