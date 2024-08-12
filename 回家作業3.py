# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:43:21 2024

@author: USER
"""

#回家作業3

while True:
    a=int(input("請輸入數字:"))
    b=a**2
    if b<50:
        print("規定範圍內")
    else:
        print("超出範圍外")
        break
print("程式執行完畢")