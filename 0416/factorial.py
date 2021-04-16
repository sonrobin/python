# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:46:44 2021

@author: User
"""

n = int(input("정수 입력 :"))

fact = 1

for i in range(1, n+1):
    fact *=i
print(n,"!은",fact,"이다.")