# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:15:02 2021

@author: User
"""

hap = 0
i = 1

while i <= 1000:
    if i%3 == 0:
        hap  += i
    i += 1
print("3의 배수들의 합 %d" % hap)