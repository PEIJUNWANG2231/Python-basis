# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:55:37 2019

@author: XPS15
"""

#Part six: iterable all situation

import sys
sys.path.append(r'D:\currencies_codes')
from foreign_exchange_part_two import AveragerGluing_5_8
from foreign_exchange_part_four import MatchUpFractals, MatchDownFractals
from foreign_exchange_part_five import EnterPoint,StopLossPoint
import numpy as np
import pandas as pd
import datetime

#遍历所有均线粘合的情况，并得出对应的结果
#df: code related dataframe
# code related list1 即AveragerGluing_5_8
#                      AveragerGluing_8_13
#                      AveragerGluing_5_8_13

def IterAveragerGluing(df,list1,s,k=1):

    #先剔除掉没有上分型和下分型的情况
    le=[]
    
    li1=MatchUpFractals(df,list1,s)
    
    for i in range(len(li1)):
        if li1[i]==0:
            le.append(i)
    
    li2=MatchDownFractals(df,list1,s)
    
    for i in range(len(li2)):
        if li2[i]==0:
            le.append(i)
    
    #理论上不存在同时没有上下分型的
    le=list(set(le))
    
    #同时再 list1，li1 和li2 里面剔除掉对应的情况
    for i in le:
        del list1[i]
        del li1[i]
        del li2[i]
        
    dict1=EnterPoint(df)
    
    dict2=StopLossPoint(df)
    
    #将dataframe变成list，每个元素对应一行
    df1=np.array(df)
    
    #li3 对应的是用的行数有多少
    li3=df1.tolist()
    
    list2=[]
    
    #进行第一步操作，是否进场
    #list2 是对应数据是否进场的集合，进场则表示为非0的数字
    for i in range(len(list1)):
        list3=[]
        for n in range(len(li3)):
            
            if list1[i]>n:
                continue
            
            if n> list1[i]+20:
                continue
            
            #当StopLoss Point 大于 enter point 则错误
            if dict2[li2[i]]>=dict1[li1[i]]:
                continue
            
            #low:4，li3[n][4]
            #当最低价低于StopLossPoint时，则不操作
            if li3[n][4] < dict2[li2[i]]:
                continue
            
            #high:3,li3[n][3]
            if li3[n][3] >= dict1[li1[i]]:
                list3.append(n)
        
        #如何没有进场，则添加0表示      
        if len(list3) ==0:
            list2.append(0)
        else:
            list2.append(list3[0])
    
    #然后再解释是否进场对应的情况
    list5=[]
    for i in range(len(list2)):
        
        list4=[]

        for n in range(len(li3)):
            if list2[i]==0:
                list4.append('no enter')

            else:
                #在list2[i]之前的数据不参与
                if list2[i]>n:
                    continue
                
                #low:4，li3[n][4]
                if li3[n][4]<dict2[li2[i]]:
                    list4.append('stop loss')
                
                m=(dict1[li1[i]]-dict2[li2[i]])
                
                #high:3,li[n][3]
                if li3[n][3]>k*m+dict1[li1[i]]:
                    list4.append(df['Time (UTC)'][n])
                
            if len(list4)==1:
                break
        
        if len(list4)==0:
            list5.append('no result')
        else:
            list5.append(list4[0])
    return list5


def Enter_date(df,list1,s):
    
    le=[]
    
    li1=MatchUpFractals(df,list1,s)
    
    for i in range(len(li1)):
        if li1[i]==0:
            le.append(i)
    
    li2=MatchDownFractals(df,list1,s)
    
    for i in range(len(li2)):
        if li2[i]==0:
            le.append(i)
    
    #理论上不存在同时没有上下分型的
    le=list(set(le))
    
    #同时再 list1，li1 和li2 里面剔除掉对应的情况
    for i in le:
        del list1[i]
        del li1[i]
        del li2[i]
        
    dict1=EnterPoint(df)
    
    dict2=StopLossPoint(df)
    
    #将dataframe变成list，每个元素对应一行
    df1=np.array(df)
    
    #li3 对应的是用的行数有多少
    li3=df1.tolist()
    
    list2=[]
    
    #进行第一步操作，是否进场
    #list2 是对应数据是否进场的集合，进场则表示为非0的数字
    for i in range(len(list1)):
        list3=[]
        for n in range(len(li3)):
            
            if list1[i]>n:
                continue
            
            if n> list1[i]+20:
                continue
            
            #当StopLoss Point 大于 enter point 则错误
            if dict2[li2[i]]>=dict1[li1[i]]:
                continue
            
            #low:4，li3[n][4]
            #当最低价低于StopLossPoint时，则不操作
            if li3[n][4] < dict2[li2[i]]:
                continue
            
            #high:3,li3[n][3]
            if li3[n][3] >= dict1[li1[i]]:
                list3.append(n)
        
        #如何没有进场，则添加0表示      
        if len(list3) ==0:
            list2.append(0)
        else:
            list2.append(list3[0])
    
    for i in range(len(list2)):
        if list2[i] == 0:
            list2[i] = 'no enter'
        else:
            list2[i] = df['Time (UTC)'][list2[i]]

    return list2

'''
   1. 粘合差值 由compare中的n决定
   2. 实体镶嵌情况，[open-close], [high-low]
   3. 第几个实体镶嵌, s决定，3个值
   4. 小实体的范围，例如1%以内，daily_pct决定，选择20个数
   5. 盈亏比，由k来决定，选择20个数
'''
def main(daily_pct=0.000799,s=0,k=1):
    start = datetime.datetime.now()
    df=pd.read_csv('D:/currencies_codes/XAUUSD/XAUUSD_Hourly_Bid.csv')
    
    '''only need to change the function to gain the result
       of 5&8, 8&13 and 5&8&13'''
    
    list1=AveragerGluing_5_8(df,daily_pct=0.000799,s=0)
    
    #无论是那种方法，所使用的循环都是一样的
    list2=IterAveragerGluing(df,list1,s,k)
    
    end = datetime.datetime.now()
    print(end-start)
    
    return list2

if __name__ == '__main__':
    main()            


list2=main(daily_pct=0.000799,s=0,k=1)
q=0
a=0
u=0
for i in list2:
    if i == 'stop loss':
        q=q+1
    elif i == 'no enter':
        a=a+1
    else:
        u=u+1

                        
u/(q+u)
                    
                
                
        
    
    


