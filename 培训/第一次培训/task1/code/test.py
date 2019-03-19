#!/usr/bin/env python
# coding=utf-8

with open("./test.txt", "w") as f:
    f.write("hello\n")
    f.write("\n")
    f.write("world\n")

with open("./test.txt", "r") as f:
    for l in f.readlines():
        l = l.strip()
        print(l)
