import os
from .key_pool import key_pool

def text_save(filename,data):
    file=open(filename,'a')
    for i in range(len(data)):
        s = str(data[i])+'\n'
        file.write(s)
    file.close()
    # print('saved')

def urlcreator(typei,geocoor,grid=(0.05,0.05),export=False):
    poi_url='restapi.amap.com/v3/place/'
    #zuoxia
    startlng=geocoor[0]
    startlat=geocoor[1]
    #youshang 
    endlng=geocoor[2]
    endlat=geocoor[3]
    dlng = -startlng+endlng
    dlat = -startlat+endlat
    Nlng = int(dlng/grid[0])+1
    Nlat = int(dlat/grid[1])+1
    keyL = key_pool()

    urlL = []
    c=0
    for i in range(Nlng):
        for j in range(Nlat):
            c=c%len(keyL)
            keyi=keyL[c]
            c+=1

            slngi=format(startlng+grid[0]*i,'.6f')
            elngi=format(startlng+grid[0]*(i+1),'.6f')
            slatj=format(startlat+grid[1]*j,'.6f')
            elatj=format(startlat+grid[1]*(j+1),'.6f')
            rec=str(slngi)+','+str(slatj)+'|'+str(elngi)+','+str(elatj)
            # print(rec)
            # keyi
            poi_rec_url=poi_url+'polygon?key='+keyi+'&polygon='+rec+'&types='+typei+'&offset=25&extensions=all&page='

            # print(poi_rec_url)
            urlL.append(poi_rec_url)
    # print('generated')
    # print(urlL)
    if export:
        text_save('urlList'+typei+'.txt',urlL)
    return urlL

def urlcreator_types(types,geocoor,grid=(0.05,0.05),export=False):
    urlD = {}
    for typei in types:
        # print(typei)
        urlD[typei] = urlcreator(typei,geocoor,grid,export)
    return urlD


if __name__ =='__main__':
    # types=['010000','020000','030000','040000','050000','060000','070000','080000','090000','100000','110000','120300','130000','170000','120100','120200','140000','150100','150200','150300','150400','150500','150600','150700','160000','200000']
    types = ['090100','090200','090300','090400','090500','090600','080100']
    geocoor = [121.393341,31.122791,121.608948,31.308944]#bottomleft, topright# 上海
    urlcreator_types(types,geocoor)