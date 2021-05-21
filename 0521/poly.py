# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:22:52 2021

@author: User
"""

import turtle as tr

t = tr.Turtle()
t.shape("turtle")

n = int(input("몇각형을 그리시겠어요:"))

for i in range(n):
    t.forward(100)
    t.left(360//n)
    
tr.exitonclick()