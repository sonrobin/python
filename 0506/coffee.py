# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:18:55 2021

@author: User
"""

coffee = 10

while True:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    
print("휴식이 길어지면 몸이 아파집니다.")