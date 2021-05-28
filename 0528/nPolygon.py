# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:38:11 2021

@author: User
"""

import turtle

t = turtle.Turtle()
t.speed(0)

def n_polygon(n,length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)
        

for i in range(18):
    t.left(20)
    n_polygon(6,100)
    
turtle.done()
turtle.bye()
    