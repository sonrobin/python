# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:17:42 2021

@author: User
"""
seq = "AATTGGCC"
def comp(seq):
    
    comp_dict = {"A":"T","T":"A","C":"G","G":"C"}
    seq_comp = ""
    for char in seq:
        seq_comp = seq_comp + comp_dict[char]
    
    return seq_comp

def rev(seq):
    seq_rev = "".join(reversed(seq))
    return seq_rev

def rev_comp(seq):
    tmp = comp(seq)
    return rev(tmp)

src = input("DNA sequence:")
cnvt = int(input("1 comp, 2 rev, 3 rev_comp:"))

if(cnvt >= 1 and cnvt <= 3):
    if cnvt == 1:
        rst = comp(seq)
    elif cnvt == 2:
        rst = rev(seq)
    else:
        rst = rev_comp(seq)
        
    print(src, "->", rst)
else:
    print("1 comp, 2 rev, 3 rev_comp:")
    
    
    
    