# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:53:20 2021

@author: User
"""

import turtle
import random


try:
    t = turtle.Turtle()
    
except:
    t = turtle.Turtle()

for i in range(30):
    length = random.randint(1,100)
    t.forward(length)
    angle = random.randint(-180,180)
    t.right(angle)


turtle.done()