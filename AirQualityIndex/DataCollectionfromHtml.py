# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:38:10 2019

@author: sairam.y
"""

import os
import time
import requests
import sys

def retrievefrom_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month < 10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)
                
            source_texts=requests.get(url)
            source_text_utf=source_texts.text.encode('utf=8')
        
            if not os.path.exists("Data/html_data/Bengaluru/{}".format(year)):
                os.makedirs("Data/html_data/Bengaluru/{}".format(year))
            with open("Data/html_data/Bengaluru/{}/{}.html".format(year,month),"wb") as output:
                output.write(source_text_utf)
            
        sys.stdout.flush()

if __name__ == "__main__":
    start_time=time.time()
    retrievefrom_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))