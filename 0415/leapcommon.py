# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:17:37 2021

@author: User
"""

num = int(input("연도입력"))
#연산자 우선순위에 따라 산술, 관계, 논리연산 순으로 연산한다.
#논리연산은 not and or 순으로 실행이 됩니다

if num % 4 == 0 and not(num%100 == 0) or num % 400:
    print(num,"윤년(leap year)입니다.")
else:
    print("평년입니다.")