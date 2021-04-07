#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   geokit.py
@Author  :   HUANG Zixun
@Version :   1.0
@Contact :   zixunhuang@outlook.com
@License :   Copyright © 2007 Free Software Foundation, Inc
@Desc    :   None
'''
import math
import numpy as np
from math import tan,atan,radians,cos,sin,asin,sqrt,atan2


def GCJ2WGS(lon, lat):
    a = 6378245.0 
    ee = 0.00669342162296594323 
    PI = 3.14159265358979324

    x = np.float64(lon) - 105.0
    y = np.float64(lat) - 35.0

    dLon = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
    dLon += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    dLon += (20.0 * math.sin(x * PI) + 40.0 * math.sin(x / 3.0 * PI)) * 2.0 / 3.0
    dLon += (150.0 * math.sin(x / 12.0 * PI) + 300.0 * math.sin(x / 30.0 * PI)) * 2.0 / 3.0

    dLat = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
    dLat += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    dLat += (20.0 * math.sin(y * PI) + 40.0 * math.sin(y / 3.0 * PI)) * 2.0 / 3.0
    dLat += (160.0 * math.sin(y / 12.0 * PI) + 320 * math.sin(y * PI / 30.0)) * 2.0 / 3.0
    radLat = lat / 180.0 * PI
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * PI)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * PI)
    wgsLon = lon - dLon
    wgsLat = lat - dLat
    return wgsLon,wgsLat



def haversine(lat_1,lng_1,lat_2,lng_2):
    lat_1,lng_1,lat_2,lng_2=map(radians,[lat_1,lng_1,lat_2,lng_2])
    dlng = lng_2-lng_1
    dlat = lat_2-lat_1
    a = sin(dlat/2)**2 + cos(lat_1)*cos(lat_2)*sin(dlng/2)**2
    c = 2*asin(sqrt(a))
    return int(c*6371*1000)

def getlngandlat(lat,lng,brng,dist):
    a=6378137
    b=6356752.3142
    f=1/298.257223563
    
    lon1=lng
    lat1=lat
    s=dist
    alpha1=radians(brng)
    sinAlpha1 = sin(alpha1)
    cosAlpha1 = cos(alpha1)
    
    tanU1 = (1-f) *tan(radians(lat1))
    cosU1 = 1 / sqrt((1 + tanU1*tanU1))
    sinU1 = tanU1*cosU1
    sigma1 = atan2(tanU1, cosAlpha1)
    sinAlpha = cosU1 * sinAlpha1
    cosSqAlpha = 1 - sinAlpha*sinAlpha
    uSq = cosSqAlpha * (a*a - b*b) / (b*b)
    A = 1 + uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)))
    B = uSq/1024 * (256+uSq*(-128+uSq*(74-47*uSq)))
    
    sigma = s / (b*A)
    sigmaP = 2*math.pi
    while (abs(sigma-sigmaP) > 1e-12):
        cos2SigmaM = cos(2*sigma1 + sigma)
        sinSigma = sin(sigma)
        cosSigma = cos(sigma)
        deltaSigma = B*sinSigma*(cos2SigmaM+B/4*(cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)-B/6*cos2SigmaM*(-3+4*sinSigma*sinSigma)*(-3+4*cos2SigmaM*cos2SigmaM)))
        sigmaP = sigma
        sigma = s / (b*A) + deltaSigma

    tmp = sinU1*sinSigma - cosU1*cosSigma*cosAlpha1
    lat2 = atan2(sinU1*cosSigma + cosU1*sinSigma*cosAlpha1,(1-f)*sqrt(sinAlpha*sinAlpha + tmp*tmp))
    lam = atan2(sinSigma*sinAlpha1, cosU1*cosSigma - sinU1*sinSigma*cosAlpha1)
    C = f/16*cosSqAlpha*(4+f*(4-3*cosSqAlpha))
    L = lam - (1-C) * f * sinAlpha *(sigma + C*sinSigma*(cos2SigmaM+C*cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)))
    revAz = atan2(sinAlpha, -tmp)
    reslng=lon1+(L*180/math.pi)
    reslat=lat2*180/math.pi
    return reslat,reslng


def bordermatching(df1,latcol1,lngcol1,df2,latcol2,lngcol2):
    minlng=max(df1[lngcol1].min(), df2[lngcol2].min())
    maxlng=min(df1[lngcol1].max(), df2[lngcol2].max())
    minlat=max(df1[latcol1].min(), df2[latcol2].min())
    maxlat=min(df1[latcol1].max(), df2[latcol2].max())

    df1=df1[(df1[lngcol1]>=minlng)&(df1[latcol1]>=minlat)&(df1[lngcol1]<=maxlng)&(df1[latcol1]<=maxlat)]
    df2=df2[(df2[lngcol2]>=minlng)&(df2[latcol2]>=minlat)&(df2[lngcol2]<=maxlng)&(df2[latcol2]<=maxlat)]
    
    df1.reset_index(drop=True,inplace=True)
    df2.reset_index(drop=True,inplace=True)
    return df1,df2