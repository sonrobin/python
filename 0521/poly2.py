# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:31:13 2021

@author: User
"""

import turtle

t = turtle.Turtle()

while True:
    
    s = turtle.textinput("","도형을 입력하세요:")
    t.reset()
    if s == "사각형":
        w = turtle.textinput("","가로:")
        w = int(w)
        
        h = turtle.textinput("", "세로:")
        h = int(h)
        
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        
        
    elif s == "삼각형":
        l = turtle.textinput("", "길이")
        l = int(l)
        
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
        
        
    elif s == "원":
        r = turtle.textinput("", "길이")
        r = int(r)
        
        turtle.circle(r)
    else:
        t.write("사각형, 삼각형, 원만 입력하세요")
    
    