# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:53:14 2021

@author: User
"""

#원의 반지름을 입력받아 면적을 리턴하는 함수를 정의하고 
#테스트하는 프로그램을 작성하세요
#단 원의 반지름은 사용자로부터 입력 받으세요!!
#단 사각형의 밑변과 높이는 사용자로부터 입력 받으세요!!

def calcArea(b,h):
    area = b*h
    return area


base = int(input("정수입력:"))
height = int(input("정수입력:"))
print("밑변과 높이가",base,height,"인 사각형의 면적은",calcArea(base,height),"입니다.")