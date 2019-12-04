# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:43:10 2019

@author: Sairam
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    temp_i=0
    average = []
    for rows in pd.read_csv('Data/AQI_data/aqi2013.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average

def avg_data_2014():
    temp_i=0
    average = []
    for rows in pd.read_csv('Data/AQI_data/aqi2014.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var = add_var + temp
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average

if __name__== "__main__":
    lst2013 = avg_data_2013()
    lst2014 = avg_data_2014()
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()