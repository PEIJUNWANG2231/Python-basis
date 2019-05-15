# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:39:33 2019

@author: XPS15
"""

#step 4 ASXPartFourMatchUpFractals
import sys
sys.path.append(r'D:\currencies_codes\XAUUSD')
from foreign_exchange_part_two import AveragerGluing_5_8,AveragerGluing_8_13,AveragerGluing_5_8_13
from foreign_exchange_part_three import UpFractal, DownFractal
import pandas as pd
import datetime

#均线粘合的最高点
#para: df, list来自AveragerGluing_5_8 等
# 每个 averager gluing 的最高点， 得出的结果是每个 情况的最高点
def AveragerGluingHighest(df,list1,s):    
    dict={}
    
    if s == 0: 
        for i in list1:
            dict[i]=max(df['High'][i],df['High'][i+1],df['High'][i+2])
    
    if s == 1:
        for i in list1:
            dict[i]=max(df['High'][i-1],df['High'][i],df['High'][i+1])
    
    if s == 2:
        for i in list1:
            dict[i]=max(df['High'][i-2],df['High'][i-1],df['High'][i])
            
    return dict

#匹配上分型
def MatchUpFractals(df,list1,s):
    #出现均线粘合的情况，keys为df中的位置，values是均线粘合三个中最高值
    dict1=AveragerGluingHighest(df,list1,s)
    
    #上分型，keys是df中的位置，values是最高值
    dict2=UpFractal(df)
    
    #开始匹配对应数值
    #list2 是对应的 均线粘合所在的df中的位置
    list2=list(dict1.keys())
    
    #list3上分型 在df里面的位置
    list3=list(dict2.keys())
    
    #有多少个粘合就有多少个与之配对的上分型
    list5=[0]*len(list2)
        
    for i in range(len(list2)):
        #每比较好一次，则更新一次list4
        list4=[]
        for k in list3:
            #保证上分型要大于均线粘合对应的三根K线的最高值
            if dict1[list2[i]]<dict2[k]:
                #当上分型的位置超过均线粘合的位置时候，则不选用
                #也就是必须要在均线粘合之前
                if k>=list2[i]:
                    continue
                #将均线粘合之前所有的上分型全部添加一起，取最后一个即为最近的上分型
                list4.append(k)
        
        #当list4存在时，则list4的最后一个分型，即为匹配分型
        if len(list4) !=0:        
            list5[i]=list4[-1]
            
        #当list4不存在时，则用0来替代，后续会删除掉0的情况
        else:
            list5[i]=0
        
    return list5

# 每个 averager gluing 的最底点， 得出的结果是每个 情况的最底点
def AveragerGluingLowest(df,list1,s):    
    dict={}
    if s == 0: 
        for i in list1:
            dict[i]=max(df['High'][i],df['High'][i+1],df['High'][i+2])
    
    if s == 1:
        for i in list1:
            dict[i]=max(df['High'][i-1],df['High'][i],df['High'][i+1])
    
    if s == 2:
        for i in list1:
            dict[i]=max(df['High'][i-2],df['High'][i-1],df['High'][i])
    return dict

#匹配下分型
def MatchDownFractals(df,list1,s):
    #出现均线粘合的情况，keys为df中的位置，values是均线粘合三个中最高值
    dict1=AveragerGluingLowest(df,list1,s)
    
    #上分型，keys是df中的位置，values是最高值
    dict2=DownFractal(df)
    
    #开始匹配对应数值
    #list2 是对应的 均线粘合所在的df中的位置
    list2=list(dict1.keys())
    
    #list3下分型 在df里面的位置
    list3=list(dict2.keys())
    
    #有多少个粘合就有多少个与之配对的下分型
    list5=[0]*len(list2)
    
    for i in range(len(list2)):
        #每比较好一次，则更新一次list4
        list4=[]
        for k in list3:
            #保证下分型要低于均线粘合对应的三根K线的最高值
            if dict1[list2[i]]>dict2[k]:
                
                #当上分型的位置超过均线粘合的位置时候，则不选用
                #也就是必须要在均线粘合之前
                if k>=list2[i]:
                    continue
                #将均线粘合之前所有的下分型全部添加一起，取最后一个即为最近的下分型
                list4.append(k)
        
        #当list4存在时，则list4的最后一个分型，即为匹配分型       
        if len(list4) !=0:        
            list5[i]=list4[-1]
        #当list4不存在时，则用0来替代，后面会删除掉0的情况
        else:
            list5[i]=0
        
    return list5

def main():
    start = datetime.datetime.now()
    
    df=pd.read_csv('D:/currencies_codes/XAUUSD/XAUUSD_Hourly_Bid.csv')
    
    list1=AveragerGluing_5_8(df)
    list2=AveragerGluing_8_13(df)
    list3=AveragerGluing_5_8_13(df)
    
    list4=MatchUpFractals(df,list1,s=0)
    list5=MatchUpFractals(df,list2,s=0)
    list6=MatchUpFractals(df,list3,s=0)
    
    list7=MatchDownFractals(df,list1,s=0)
    list8=MatchDownFractals(df,list2,s=0)
    list9=MatchDownFractals(df,list3,s=0)
    
    #仅做5_8的例子
    li1=[0]*len(list1)
    
    for i in range(len(li1)):
        li1[i] = df['Time (UTC)'][list1[i]]
    
    li2=[0]*len(list4)
    
    for i in range(len(li2)):
        li2[i] = df['Time (UTC)'][list4[i]]
    
    li3=[0]*len(list7)
    
    for i in range(len(li2)):
        li3[i] = df['Time (UTC)'][list7[i]]
    
    result= pd.DataFrame(
    {'AveragerGluing_5_8': li1,
     'AveragerGluing_5_8_index': list1,
     'MatchUpFractals': li2,
     'MatchUpFractalsindex': list4,
     'MatchDownFractals': li3,
     'MatchDownFractalsindex': list7,
    })
    
    # the csv file provide the chance to data visualization
    result.to_csv('D:/Match Fractal result.csv')
    
    end = datetime.datetime.now()
    print(end-start)

if __name__ == '__main__':
    main()
