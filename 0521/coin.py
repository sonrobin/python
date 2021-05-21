# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:09:32 2021

@author: User
"""

import turtle as t
import random

screen = t.Screen()

img1 = "C:\\Users\\User\\Documents\\파이썬\\0521\\front.gif"
img2 = "C:\\Users\\User\\Documents\\파이썬\\0521\\back.gif"

screen.addshape(img1)
screen.addshape(img2)

t1 = t.Turtle()
while True:
    t.delay(5)
    coin = random.randint(0,1)
    if coin == 0:
        t1.shape(img1)
        t1.stamp()
        
    elif coin == 1:
        t1.shape(img2)
        t1.stamp()
    
    