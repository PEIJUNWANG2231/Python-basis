# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:14:44 2018

@author: XPS15
"""

def order(list=[]):
    number=[]
    for i in range(0,len(list),1):
        n=max(list)
        number.append(n)
        list.remove(max(list))
    return number
   
    
