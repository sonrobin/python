# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:22:09 2021

@author: User
"""

import turtle

t = turtle.Turtle()

for i in range(6):
    t.circle(100)
    t.left(360/6)
    
t.exitonclick()