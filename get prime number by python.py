# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:22:27 2018

@author: XPS15
"""

import math
def prime(n):
    number=[]
    prime_number=[]
    for i in range(0,n,1):
        number.append(True)
    number[0] =False
    number[1] =False
    print(number)
    for i in range(2, int(math.sqrt(n)),1):
        for j in range(i*i, n, i):
            number[j]=False
    for i in range(0, n, 1):
        if number[i]==True:
            prime_number.append(i)
    return prime_number

print(prime(100))
        
    
