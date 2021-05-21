# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:24:19 2021

@author: User
"""

import turtle as t

t.shape('turtle')

t.penup()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0,0)
t.pendown()
s = t.textinput("", "숫자 입력:")
n = int(s)

if n > 0:
    t.goto(100,100)
elif n == 0:
    t.goto(100,0)
elif n < 0:
    t.goto(100,-100)
    
t.exitonclick()