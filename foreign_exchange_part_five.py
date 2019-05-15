# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:07:03 2019

@author: XPS15
"""

import sys
sys.path.append(r'D:\currencies_codes')
from foreign_exchange_part_three import UpFractal, DownFractal

#微调所有上分型，变为进场价格
def EnterPoint(df):
    dict1=UpFractal(df)

    
    list1=list(dict1.keys())
    
    for i in list1:
        dict1[i]=round(dict1[i],2)
    
    str_open = str(df['Open'][0])
    
    li1=[-3,-4,-5,-6]
    
    for k in li1:
        if str_open[k] == '.':
            for i in list1:
                dict1[i]=round(dict1[i],abs(k)-1)
                if dict1[i]*(10**(abs(k)-1))%5==0:
                            dict1[i]=dict1[i]+1/(10**(abs(k)-1))
                            dict1[i]=round(dict1[i],abs(k)-1)
                else:
                    dict1[i]=((int(dict1[i]*(10**(abs(k)-1))/5)+1)*5+1)/(10**(abs(k)-1))
    return dict1

#微调所有下分型，变为止损价格
def StopLossPoint(df):
    dict1=DownFractal(df)
    
    list1=list(dict1.keys())
    
    for i in list1:
        dict1[i]=round(dict1[i],2)
    
    str_open = str(df['Open'][0])
    
    li1=[-3,-4,-5,-6]
    
    for k in li1:
        if str_open[k] == '.':
            for i in list1:
                dict1[i]=round(dict1[i],abs(k)-1)
                if dict1[i]*(10**(abs(k)-1))%5==0:
                            dict1[i]=dict1[i]-1/(10**(abs(k)-1))
                            dict1[i]=round(dict1[i],abs(k)-1)
                else:
                    dict1[i]=(int(dict1[i]*(10**(abs(k)-1))/5)*5-1)/(10**(abs(k)-1)) 
    return dict1
