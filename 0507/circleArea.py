# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:35:08 2021

@author: User
"""

def calArea(radius):
    area = 3.14159 * radius * radius
    return area

#파라미터는 여러개가 있을 수 있지만 리턴되는 값은 하나입니다.

cir1Radius = 5
cir2Radius = 10
cir3Radius = 20

cir1Area = calArea(cir1Radius)
cir2Area = calArea(cir2Radius)
cir3Area = calArea(cir3Radius)

print("%d 번째 원의 면적은 %f 입니다." % (1, cir1Area))
print(2,"번째 원의 면적은 ",cir2Area,"입니다.")
print("{0} 번째 원의 면적은 {1} 입니다." .format(3, cir3Area))