# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:09:49 2021

@author: User
"""

arr = []
num = 0
hap = 0

for i in range(5):
    scr = int(input("%d번 학생 점수 입력:" % (i+1)))
    arr.append(scr)
    
    
for i in arr:
    num += 1
    hap += i
    if i >= 60:
        print("%d번 학생은 점수는 %d 이고 합격입니다." % (num,i))
    else:
        print("%d번 학생은 점수는 %d 이고 불합격입니다." % (num,i))
        
print("총합은 %d 이고 평균은 %0.1f 입니다." % (hap,(hap/num)))
        
    