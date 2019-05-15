# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:29:15 2019

@author: XPS15
"""
# all the currenceies
# step 1
# Data preparation of further data manipulating 
# save the CSV in local laptop 

import pandas as pd
import numpy as np
import datetime

#SMA is a type of MA, it could be call by talib
#n represent for period

def SMA(close,n,m=1):
    result = np.array([np.nan]*len(close))
    result[n-2]=close[:n-1].mean()
    for i in range(n-1,len(close)):
        result[i]=(m*close[i]+(n-m)*result[i-1])/n
    return result

#basic operation of financial market data from Yahoo APIs
"""n is to adjust the compare, 
   balancing the momentum effect"""

def Alligator(df,n=1):
    
    df['Var1']=(df['High']+df['Low'])/2
    
    average=[5,8,13] #fibonacci squence:5,8,13 
    moves=[3,5,8]
    names=['jaw','teeth','lips']
    
    #produce the three SMA: 5,8,13, and shift forward 3,5,8 unit
    for i in range(3):
        df[names[i]]=SMA(df['Var1'],average[i])
        df[names[i]]=df[names[i]].shift(periods=moves[i])
    
    df['5&8']=df['jaw']-df['teeth']
    df['8&13']=df['teeth']-df['lips']
    df['5&8']=abs(df['5&8'])
    df['8&13']=abs(df['8&13'])
    
    #均线粘合的差值由close来决定
    
    #compare data is decided by the close price
    
    #df['compare']=((df['Close']/10).astype(int)+n)*0.01, used in gold
    
    df['compare']=df['Close']/1000
      
    df['daily_pct']=abs(df['Open']-df['Close'])/df['Close']
    
    df=df.dropna()
    return df


#use API to get the related data by code
def main():
    start = datetime.datetime.now()
    
    df=pd.read_csv('D:/currencies_codes/XAUUSD/XAUUSD_Hourly_Bid.csv')
    df=Alligator(df)
    df.to_csv('D:/currencies_codes/XAUUSD/XAUUSD_Hourly_Bid.csv')
    
    end = datetime.datetime.now()
    print(end-start)
    return df

if __name__ == '__main__':
    main()

  
    