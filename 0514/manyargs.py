# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:50:03 2021

@author: User
"""

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4))
print(add_many(1,2,3,4,5,6,7,8,9,10))