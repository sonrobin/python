# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:39:36 2021

@author: User
"""

#dictionary는 Key:value 쌍으로 자료를 저장합니다.
#dictionarysms 숫자로 인덱싱 할 수 없고
#키값으로 밸류에 접근할 수 있습니다.

a = dict()

a['name'] = 'python' # 키값으로 문자열 가능
a[('a',)] = 'python' # 키값으로 튜플 가능(변경되지않아서)
#a[[1]] = 'python' # error 키값으로 리스트 불가능
a[250] = 'python' # 키값으로 정수 가능

print(a)

# filename : dictEx.py