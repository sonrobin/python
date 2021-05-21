# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:15:48 2021

@author: User
"""

import turtle as t
t.shape('turtle')

color = ['yellow','red','green','blue']

for i in range(len(color)):
    t.pendown()
    t.fillcolor(color[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()
    t.forward(50)
t.exitonclick()