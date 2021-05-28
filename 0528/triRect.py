# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:29:26 2021

@author: User
"""

import turtle

t = turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.right(360/3)
    
t.penup()
t.forward(200)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(360/4)
    
turtle.done()