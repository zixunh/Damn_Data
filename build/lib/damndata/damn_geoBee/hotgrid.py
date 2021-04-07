#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hotgrid.py
@Author  :   HUANG Zixun
@Version :   1.0
@Contact :   zixunhuang@outlook.com
@License :   Copyright © 2007 Free Software Foundation, Inc
@Desc    :   None
'''

import numpy as np
import pandas as pd
from .geokit import getlngandlat, haversine




class HotGridGenerator():
    def __init__(self,gridUnit,searchRadius):
        self.gridUnit=gridUnit
        self.searchRadius=searchRadius
        self.indexList=[]
        self.colList=[]
        self.gridCenter=pd.DataFrame(index=self.indexList, columns=self.colList)

    def grid_setting(self,df,latcol,lngcol):
        gU=self.gridUnit
        sR=self.searchRadius
        bleed=int(sR/gU)

        minlng=df[lngcol].min()
        maxlng=df[lngcol].max()
        minlat=df[latcol].min()
        maxlat=df[latcol].max()
        
        midlat=(maxlat+minlat)/2
        midlng=(maxlng+minlng)/2
        dx=haversine(minlat,maxlng,minlat,minlng)
        dy=haversine(minlat,maxlng,maxlat,maxlng)

        lngL=[]
        latL=[]
        for i in range(bleed,int(dx/gU)-bleed+1):
            dist=i*gU
            tlat,tlng=getlngandlat(minlat,minlng,90,dist)
            lngL.append(tlng)
        for i in range(bleed,int(dy/gU)-bleed+1):
            dist=i*gU
            tlat,tlng=getlngandlat(minlat,minlng,0,dist)
            latL.append(tlat)

        self.indexList=[]
        self.colList=[]
        for k in range(0,len(latL)):
            self.indexList.append(str(k).zfill(3))
        for k in range(0,len(lngL)):
            self.colList.append(str(k).zfill(3))
        self.gridCenter = pd.DataFrame(index=self.indexList, columns=self.colList)
        for i in range(0,len(latL)):
            for j in range(0,len(lngL)):
                self.gridCenter.iloc[i,j]=(latL[i],lngL[j])
        self.gridCenter.sort_index(axis=0,ascending=False).describe()

        return self.indexList,self.colList,self.gridCenter

    def gridCounting_basic(self,df0,lat_col,lng_col):
        df_typei=df0
        counting = pd.DataFrame(index=self.indexList, columns=self.colList)
        for i in range(0,len(self.indexList)):
            for j in range(0,len(self.colList)):
                gci=self.gridCenter.iloc[i,j]

                t,maxlng_ij=getlngandlat(gci[0],gci[1],90,self.searchRadius)
                t,minlng_ij=getlngandlat(gci[0],gci[1],90,-self.searchRadius)
                maxlat_ij,t=getlngandlat(gci[0],gci[1],0,self.searchRadius)
                minlat_ij,t=getlngandlat(gci[0],gci[1],0,-self.searchRadius)
                df_typei_ij=df_typei[(df_typei[lat_col]>=minlat_ij)&(df_typei[lat_col]<=maxlat_ij)&(df_typei[lng_col]>=minlng_ij)&(df_typei[lng_col]<=maxlng_ij)]

                distL=list(map(lambda x,y:haversine(x,y,lat_2=gci[0],lng_2=gci[1]),df_typei_ij[lat_col],df_typei_ij[lng_col]))
                boolL=list(filter(lambda x:x<=self.searchRadius,distL))
 
                counting.iloc[i,j]=len(boolL)
        return counting.astype(float)


    def gridCounting_byType(self,df0,lat_col,lng_col,type_col):
        counting_list = []
        for typei in np.sort(df0[type_col].unique()):
            df_typei=df0[df0[type_col]==typei]

            counting = self.gridCounting_basic(df_typei,lat_col,lng_col)
            counting_list.append(counting.astype(float))
        return counting_list

    def gridCounting_weight(self,df0,lat_col,lng_col, weight_col):
        df_typei=df0
        counting = pd.DataFrame(index=self.indexList, columns=self.colList)
        for i in range(0,len(self.indexList)):
            for j in range(0,len(self.colList)):
                gci=self.gridCenter.iloc[i,j]
  
                t,maxlng_ij=getlngandlat(gci[0],gci[1],90,self.searchRadius)
                t,minlng_ij=getlngandlat(gci[0],gci[1],90,-self.searchRadius)
                maxlat_ij,t=getlngandlat(gci[0],gci[1],0,self.searchRadius)
                minlat_ij,t=getlngandlat(gci[0],gci[1],0,-self.searchRadius)
                df_typei_ij=df_typei[(df_typei[lat_col]>=minlat_ij)&(df_typei[lat_col]<=maxlat_ij)&(df_typei[lng_col]>=minlng_ij)&(df_typei[lng_col]<=maxlng_ij)].copy()
   
                df_typei_ij.loc[:,'dist']=list(map(lambda x,y:haversine(x,y,lat_2=gci[0],lng_2=gci[1]),df_typei_ij[lat_col],df_typei_ij[lng_col]))
                df_typei_bool=df_typei_ij[df_typei_ij.loc[:,'dist']<=self.searchRadius].copy()
                counting.iloc[i,j]=df_typei_bool.loc[:,weight_col].sum()
 
        return counting.astype(float)

    def gridCounting_ex(self,df0,lat_col,lng_col,weight_col,type_col):
        counting_list = []
        for typei in np.sort(df0[type_col].unique()):
            df_typei=df0[df0[type_col]==typei]

            counting = self.gridCounting_weight(df_typei,lat_col,lng_col,weight_col)
            counting_list.append(counting.astype(float))
        return counting_list
 
    @staticmethod
    def hotarray(df0,colname):
        idL=[]
        for i in range(0,df0.shape[0]):
            for j in range(0,df0.shape[1]):
                idL.append('grid'+str(i).zfill(3)+'-'+str(j).zfill(3))
                
        df1=pd.DataFrame(index=idL,columns=[colname])
        c=0
        for i in range(0,df0.shape[0]):
            for j in range(0,df0.shape[1]):

                df1.loc[idL[c],colname]=df0.iloc[i,j]
                c+=1
        return df1.astype(float)


