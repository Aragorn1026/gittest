#!/usr/bin/env python
# -*- coding: UTF-8 -*-

print("---------猜数字---------")
index = 0
while True:
    number = input("输入你猜的数字：")
    guess = int(number)
    index += 1
    if guess == 8:
        print("恭喜！猜对了！数字是8！猜了",index,"次！")
        break
    elif guess > 8:
        print("你猜的数字大了！")
        continue
    else:
        print("你猜的数字小了！")
        continue
