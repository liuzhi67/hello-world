#!/usr/bin/env python
# coding=utf-8

name_dct = {"北京":"a", "上海":"b", "广州":"c", "武汉":"d"}
name_dct2 = {"a":"北京", "b":"长沙", "c":"成都", "d":"武汉"}
print(name_dct)
print("北京" in name_dct)
name = "北京"
print(type(name))
print(name in name_dct)

print("-------------")
for k, v in name_dct2.items():
    if k != '' and v in name_dct:
        print(v in name_dct)
        print(k, v)
