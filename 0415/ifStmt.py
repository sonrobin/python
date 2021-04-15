# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:46:29 2021

@author: User
"""
# filename : ifStmt.py
# ifStmt
# 1. if 조건문
# 2. if 조건문 else
# 3. if 조건문 elif 조건문  elif 조건문 .. else

num = int(input("나이 입력 : "))
money = 10000

if num > 20:
    money +=  5000 # money = money + 5000
    
print("당신의 입장료는",money,"입니다.")
    