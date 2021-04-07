#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   amapoiCollector_1.1.py
@Time    :   2020/01/11 23:37:44
@Author  :   Huang Zixun 
@Version :   1.1
@Contact :   zixunhuang@outlook.com
'''
from urllib import request
import json
import pandas as pd
import csv,math
import numpy as np
from .GCJ02_to_WGS84 import GCJ2WGS

def getpoi_page(poi_search_url, page):
    req_url = 'http://'+poi_search_url+str(page)
    data = ''
    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
    return data
def hand(poilist, result):
    pois = result['pois']
    for i in range(len(pois)):
        poilist.append(pois[i])
def getpois(poi_search_url,display=0):
    i = 1
    poilist = []
    while True:  
        result = getpoi_page(poi_search_url, i)
        # print('Scraping...\n')
        result = json.loads(result)
        if display:
            print(result)
        if result.get('count','not exist') == 'not exist':
            break
        if result.get('count','not exist') == '0':
            break
        hand(poilist, result)
        i = i + 1
    return poilist
def write_to_csv(poilist,filepath):
    x=[]
    for i in range(len(poilist)):
        gcjlng=poilist[i]['location'].split(",")[0]
        gcjlat=poilist[i]['location'].split(",")[1]
        wgslng,wgslat=GCJ2WGS(gcjlng,gcjlat)
        x.append([poilist[i]['id'],poilist[i]['name'],wgslng,wgslat, poilist[i]['adname'],poilist[i]['biz_ext'].get('cost','unknown'),poilist[i]['biz_ext'].get('rating','unknown'),poilist[i]['type']])
    c=pd.DataFrame(x,columns=['id','name','wgslng','wgslat','adname','cost','rating','type'])
    c.to_csv(filepath,encoding='utf-8')

