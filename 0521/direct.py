# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:40:45 2021

@author: User
"""

import turtle as t

t.width(3)

t.shapesize(3,3)

while True:
    command = t.textinput("","명령을 입력하세요:")
    if command == 'l':
        t.left(90)
        t.forward(100)
    if command == 'r':
        t.right(90)
        t.forward(100)
    