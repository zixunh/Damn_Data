# Brief Intro
The third-party package (**damndata**) is currently divided into two parts, one part is used for obtaining urban big data such as points of interest, area of interest, social media data with geo-information, and the other part is used for extracting geographic distribution features to help designers visualize mass urban information.
# Installation
```python
python setup.py install
```
---
# Damn GeoSpider
### GeoAutoNavi
### GeoSocialMedia
# Damn GeoBee
### GeoKit
- GCJ2WGS
- haversine
- getlngandlat
- bordermatching
### HotGrid.HotGridGenerator
- gridUnit
- searchRadius
- grid_setting
- gridCounting_basic
- gridCounting_weight
- gridCounting_byType
- gridCounting_ex
- hotarray
### GeoHash
# How to Use it
### Example 1
```python
from damndata.damn_geoSpider import geoautonavi as amaPoi
import pandas as pd
```
```python
http      = 'restapi.amap.com/v3/place/around?'
key       = 'key= GET_YOUR_KEY_FROM_THIS_WEBSITE: https://lbs.amap.com/api/'
para_loc  = '&location=120.233851,30.167682&radius=800'
para_type = '&types=050000|070000|090000|120300|141200|160000|170100|170200'
```
```python
URL=http+key+para_loc+para_type+'&output=json&offset=25&extensions=all&page='
pois=amaPoi.getpois(URL)                                                    
filePath = 'E:/zixunHUANG/2019-2021_Project/202007_FridaySalonSharing/week200724/test.csv'
amaPoi.write_to_csv(pois,filePath)                                        
```
```python
df=pd.read_csv(filePath,index_col='Unnamed: 0')
df
```
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>wgslng</th>
      <th>wgslat</th>
      <th>adname</th>
      <th>cost</th>
      <th>rating</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>B0GUYZ2ME5</td>
      <td>简鹿糖水铺金湖艺境城店</td>
      <td>120.228993</td>
      <td>30.170145</td>
      <td>萧山区</td>
      <td>16.00</td>
      <td>3.5</td>
      <td>餐饮服务;甜品店;甜品店</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B0FFJNT73W</td>
      <td>都会艺境售楼处</td>
      <td>120.229098</td>
      <td>30.170268</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B0GUM7859O</td>
      <td>朝天门火锅(杭州湘湖店)</td>
      <td>120.229051</td>
      <td>30.170334</td>
      <td>萧山区</td>
      <td>119.00</td>
      <td>5.0</td>
      <td>餐饮服务;中餐厅;火锅店</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>B0FFLOY0Q3</td>
      <td>萧山区湘湖幼儿园休博园分园</td>
      <td>120.229016</td>
      <td>30.165172</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>科教文化服务;学校;幼儿园</td>
    </tr>
    <tr>
      <th>71</th>
      <td>B0FFFYK6WV</td>
      <td>伊然美发</td>
      <td>120.230740</td>
      <td>30.175009</td>
      <td>萧山区</td>
      <td>85.00</td>
      <td>5.0</td>
      <td>生活服务;美容美发店;美容美发店</td>
    </tr>
    <tr>
      <th>72</th>
      <td>B023B18JV6</td>
      <td>益万家连锁药店(湘湖店)</td>
      <td>120.230940</td>
      <td>30.174997</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>医疗保健服务;医药保健销售店;药房</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 8 columns</p>
</div>

### Example 2
```python
type_list=['050000','060000','070000']
```
```python
for i,typei in enumerate(type_list):
    print(i,typei)
    URL_i=http+key+para_loc+typei+'&output=json&offset=25&extensions=all&page='
    pois_i=amaPoi.getpois(URL_i)                                                           
    filePath_i = 'E:/zixunHUANG/2019-2021_Project/202007_FridaySalonSharing/week200724/'+str(i).zfill(2)+'.csv'
    amaPoi.write_to_csv(pois_i,filePath_i)                                                 
    print('Done!!!')
```
### Example 3
```python
import pandas as pd
chengdu_poi = pd.read_csv('chengdu_poi.csv').drop(columns='Unnamed: 0')
chengdu_poi.tail(1)
```
![26a8c13e33f7e264966a6f6b452f6be](https://user-images.githubusercontent.com/39406532/113282997-428e8000-931a-11eb-9a9b-ebf7a0294d56.png)
```python
from damndata.damn_geoBee.hotgrid import HotGridGenerator
hg = HotGridGenerator(gridUnit = 200,searchRadius = 1000)
hg.grid_setting(chengdu_poi,'wgslat','wgslng')
chengdu_poi_hotMap=hg.gridCounting_basic(chengdu_poi,'wgslat','wgslng')
```
```python
import seaborn as sns
from IPython.core.pylabtools import figsize
figsize(21,16)
sns.heatmap(chengdu_poi_hotMap.sort_index(axis=0,ascending=False))
```

![example1](https://user-images.githubusercontent.com/39406532/113274748-9bf1b180-9310-11eb-83f9-f551c0aa93df.png)

### Example 4
```python
hg = HotGridGenerator(gridUnit = 1000,searchRadius = 1000)
hg.grid_setting(chengdu_poi,'wgslat','wgslng')
chengdu_typeMap = hg.gridCounting_byType(chengdu_poi,'wgslat','wgslng','typei')
```
```python
import matplotlib.pyplot as plt
%matplotlib inline
fig,ax = plt.subplots(4,4, figsize=(21,12))
c=0
for i in range(4):
    for j in range(4):
        sns.heatmap(chengdu_typeMap[c].sort_index(axis=0,ascending=False),ax=ax[i,j])
        ax[i,j].set_title('poi'+str(c).zfill(2))
        c+=1
plt.tight_layout()
```
![example2](https://user-images.githubusercontent.com/39406532/113274997-dd825c80-9310-11eb-95b6-3abc37ae069d.png)

---
**Email:** huangzxarchitecture@zju.edu.cn

**Ins:** zixun_huang.arch
