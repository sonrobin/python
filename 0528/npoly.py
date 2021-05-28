# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:41:08 2021

@author: User
"""

import turtle as t

s = t.textinput("input","몇 각형을 원하세요:")
n = int(s)

for i in range(n):
    t.forward(50)
    t.left(360/n)
    
t.done()