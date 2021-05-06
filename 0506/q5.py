# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:42:29 2021

@author: User
"""

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

hap = 0

for i in score:
    hap += i
    
print("평균: %0.1f" % (hap/len(score)))