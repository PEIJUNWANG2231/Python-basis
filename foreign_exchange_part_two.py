# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:14:43 2019

@author: XPS15
"""

# step 2 XAUUSD
# select the implications of momentum effect

from interval import Interval
import pandas as pd
import datetime
import numpy as np

# example: 5&8均线粘合
#para: dataframe,target:8&13,daily_pct:实体大小,
#when change target, 实体镶嵌也要修改
#s 代表第几根均线粘合，0是代表第一根
# daily_pct 是25%的数
def AveragerGluing_5_8(df,daily_pct=0.000799,s=0):
    #将dataframe拆开，拆成list操作
    df1=np.array(df)

    li=df1.tolist()
    
    #target represent 5&8, 8&13
    #5&8:11，8&13:12,compare:13
    #example: 5&8 <= compare
    list1=[]
    for i in range(0,len(li)-2):
        if li[i][11]<=li[i][13]:
            if li[i+1][11]<=li[i+1][13]:
                if li[i+2][11]<=li[i+2][13]:
                    list1.append(i)
    
    #open:2，close:5,
    #5&8 对应的实体镶嵌则是镶嵌在jaw：8 & teeth：9 上
    #8&13 对应的实体镶嵌则是在 teeth：9 & lips：10 上
    list2=[]
    for i in list1:
        #k 对应开盘价和收盘价
        k=[li[i+s][2],li[i+s][5]]
        m=Interval(min(k),max(k))
        
        if li[i+s][8] in m:
            if li[i+s][9] in m:
                list2.append(i)
    
    list2=list(set(list2))
    
    #daily_pct:14
    list3=[]
    for i in list2:
        if li[i][14]<=daily_pct:         
            list3.append(i)

    list3=list(set(list3))
    list3.sort()
    return list3
    
    
# example: 8&13均线粘合
#para: dataframe,target:8&13,daily_pct:实体大小,
#when change target, 实体镶嵌也要修改
def AveragerGluing_8_13(df,s=0,daily_pct=0.000799):
    #将dataframe拆开，拆成list操作
    df1=np.array(df)

    li=df1.tolist()
    
    #target represent 5&8, 8&13
    #5&8:11，8&13:12,compare:13
    #example: 5&8 <= compare
    list1=[]
    for i in range(0,len(li)-2):
        if li[i][12]<=li[i][13]:
            if li[i+1][12]<=li[i+1][13]:
                if li[i+2][12]<=li[i+2][13]:
                    list1.append(i)
                        
    #open:2，close:5,
    #5&8 对应的实体镶嵌则是镶嵌在jaw：8 & teeth：9 上
    #8&13 对应的实体镶嵌则是在 teeth：9 & lips：10 上
    list2=[]
    for i in list1:
        k=[li[i+s][2],li[i+s][5]]
        m=Interval(min(k),max(k))
        
        if li[i+s][9] in m:
            if li[i+s][10] in m:
                list2.append(i)
 
    #daily_pct:14
    list3=[]
    for i in list2:
        if li[i][14]<=daily_pct:         
            list3.append(i)

    list3=list(set(list3))
    list3.sort()
    return list3

# example: 5&8&13均线粘合,三线粘合
#para: dataframe,target:5&&13,daily_pct:实体大小,
#when change target, 实体镶嵌也要修改
def AveragerGluing_5_8_13(df,s=0,daily_pct=0.000799):
    #将dataframe拆开，拆成list操作
    df1=np.array(df)

    li=df1.tolist()
    
    #target represent 5&8, 8&13
    #5&8:11，8&13:12,compare:13
    #example: 5&8 <= compare
    list1=[]
    for i in range(0,len(li)-2):
        if li[i][11]<=li[i][13]:
            if li[i+1][11]<=li[i+1][13]:
                if li[i+2][11]<=li[i+2][13]:
                    list1.append(i)
    
    #example: 8&13 <= compare
    list2=[]
    for i in range(0,len(li)-2):
        if li[i][12]<=li[i][13]:
            if li[i+1][12]<=li[i+1][13]:
                if li[i+2][12]<=li[i+2][13]:
                    list2.append(i)
    
    #gain the intersection of list1 and list2
    li1=list(set(list2).intersection(set(list1)))
    
    #open:2，close:5,
    #5&8 对应的实体镶嵌则是镶嵌在jaw：8 & teeth：9 上
    #8&13 对应的实体镶嵌则是在 teeth：9 & lips：10 上
    list3=[]
    for i in li1:
        k=[li[i+s][2],li[i+s][5]]
        
        m=Interval(min(k),max(k))
        
        if li[i+s][8] in m:
            if li[i+s][9] in m:
                if li[i+s][10] in m:
                    list3.append(i)

    #daily_pct:14
    list4=[]
    for i in list3:
        if li[i][14]<=daily_pct:         
            list4.append(i)

    list4=list(set(list4))
    list4.sort()
    return list4

def main():
    start = datetime.datetime.now()
    df=pd.read_csv('D:/currencies_codes/XAUUSD/XAUUSD_Hourly_Bid.csv')
    list1=AveragerGluing_5_8(df)
    list2=AveragerGluing_8_13(df)
    list3=AveragerGluing_5_8_13(df)
    print(list1,list2,list3)
    end = datetime.datetime.now()
    print(end-start)
    return list1, list2, list3

