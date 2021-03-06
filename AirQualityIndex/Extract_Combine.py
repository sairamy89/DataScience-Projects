# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 06:28:56 2019

@author: Sairam
"""

from AQI_Plotting import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016
import requests
import sys
import pandas as pd
import os
import csv
from bs4 import BeautifulSoup


def meta_data(month, year):
    html_file = open('Data/html_data/New Delhi/{}/{}.html'.format(year,month), 'rb')
    plain_text = html_file.read()
    
    tempData = []
    finalData = []
    
    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class' : 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempData.append(a)
                
    rows = len(tempData) / 15
    
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempData[0])
            tempData.pop(0)
        finalData.append(newtempD)
        
    length = len(finalData)
    
    finalData.pop(length - 1)
    finalData.pop(0)
    
    for a in range(len(finalData)):
        finalData[a].pop(6)
        finalData[a].pop(13)
        finalData[a].pop(12)
        finalData[a].pop(11)
        finalData[a].pop(10)
        finalData[a].pop(9)
        finalData[a].pop(0)
        
    return finalData

def data_combine(year, cs):
    for a in pd.read_csv('Data/Real_Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Real_Data/"):
        os.makedirs("Data/Real_Data")
    for year in range(2013, 2017):
        final_data = []
        with open('Data/Real_Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1, 13):
            temp = meta_data(month, year)
            final_data = final_data + temp
        
        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()
        #pm = avg_data(year)
        
        if len(pm) == 364:
            pm.insert(364, '-')
            
        for i in range(len(final_data)-1):
            final_data[i].insert(8, pm[i])
        
        with open('Data/Real_Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag=0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                    
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
     
    total=data_2013+data_2014+data_2015+data_2016
    
    with open('Data/Real_Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
        
df=pd.read_csv('Data/Real_Data/Real_Combine.csv')