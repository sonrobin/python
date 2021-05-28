# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:25:18 2021

@author: User
"""

import turtle

t = turtle.Turtle()

def drawRect(length):
    for i in range(4):
        t.forward(length)
        t.right(90)
        
for i in range(-200,400,200):
    t.up()
    t.goto(i,0)
    t.down()
    drawRect(100)



turtle.done()
turtle.bye()