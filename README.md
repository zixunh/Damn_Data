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
import pandas as pd
chengdu_poi = pd.read_csv('chengdu_poi.csv').drop(columns='Unnamed: 0')
chengdu_poi.tail(1)
```
![26a8c13e33f7e264966a6f6b452f6be](https://user-images.githubusercontent.com/39406532/113276699-add45400-9312-11eb-82b2-5f9658afcdc0.png)
```python
from damndata.damn_geoBee.hotgrid import HotGridGenerator
hg = HotGridGenerator(gridUnit = 200,searchRadius = 1000)
hg.grid_setting(chengdu_poi,'wgslat','wgslng')
chengdu_poi_hotMap=hg.gridCounting_basic(chengdu_poi,'wgslat','wgslng')
```
```python
import seaborn as sns
from IPython.core.pylabtools import figsize
figsize(21,12)
sns.heatmap(chengdu_poi_hotMap.sort_index(axis=0,ascending=False))
```
![example1](https://user-images.githubusercontent.com/39406532/113274748-9bf1b180-9310-11eb-83f9-f551c0aa93df.png)

### Example 2
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
##### example

### 载入环境


```python
import amaPoi
import pandas as pd
```

### 参数设置

###### 说明**
详细文档：         https://lbs.amap.com/api/webservice/guide/api/search 

http接口：         'resapi.amap.com/v3/place/'

检索模式：（地理参数 'geo'）

关键字搜索：        'text?'     >>>  'city=' (citycode|adcode)

周边搜索：         'around?'    >>>  'location='、'radius='

多边形搜索：        'polygon?'   >>>  'polygon=' 

参数：             key、'geo'、types|keywords


```python
http      = 'restapi.amap.com/v3/place/around?'
key       = 'key=f9257dab1e8214b074587fe16484cb1e'
para_loc  = '&location=120.233851,30.167682&radius=800'
para_type = '&types=050000|070000|090000|120300|141200|160000|170100|170200'
```

### 爬取


```python
URL=http+key+para_loc+para_type+'&output=json&offset=25&extensions=all&page='
pois=amaPoi.getpois(URL)                                                           #请求数据

filePath = 'E:/zixunHUANG/2019-2021_Project/202007_FridaySalon/week200724/test.csv'#设定文件路径
amaPoi.write_to_csv(pois,filePath)                                                 #写入本地
print('Done!!!')
```

    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Done!!!
    

### 读入爬取结果


```python
df=pd.read_csv(filePath,index_col='Unnamed: 0')
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <td>B0GRAZ3QZY</td>
      <td>肯德基</td>
      <td>120.228988</td>
      <td>30.170157</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>餐饮服务;快餐厅;快餐厅</td>
    </tr>
    <tr>
      <th>2</th>
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
      <th>3</th>
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
      <th>4</th>
      <td>B0GR1ZXHKS</td>
      <td>都会艺境商业街招商部</td>
      <td>120.228925</td>
      <td>30.170261</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>5</th>
      <td>B0GDD7UITV</td>
      <td>一点点(金湖艺境城店)</td>
      <td>120.228902</td>
      <td>30.170082</td>
      <td>萧山区</td>
      <td>11.00</td>
      <td>4.9</td>
      <td>餐饮服务;餐饮相关场所;餐饮相关</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B0FFKXUMCW</td>
      <td>古茗湘湖店</td>
      <td>120.228872</td>
      <td>30.170117</td>
      <td>萧山区</td>
      <td>12.00</td>
      <td>4.9</td>
      <td>餐饮服务;冷饮店;冷饮店</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B0FFLI4TAW</td>
      <td>菜鸟驿站(杭州广宁小区蜀山路427号店菜鸟驿)</td>
      <td>120.229666</td>
      <td>30.170505</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;物流速递;物流速递</td>
    </tr>
    <tr>
      <th>8</th>
      <td>B0FFHI50J1</td>
      <td>萧山(地铁湘湖站)旅游咨询点</td>
      <td>120.229562</td>
      <td>30.170655</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>9</th>
      <td>B0GDVS7DLM</td>
      <td>宝哥面(湘湖店)</td>
      <td>120.228871</td>
      <td>30.170482</td>
      <td>萧山区</td>
      <td>21.00</td>
      <td>3.5</td>
      <td>餐饮服务;中餐厅;中餐厅</td>
    </tr>
    <tr>
      <th>10</th>
      <td>B0FFJCYS9V</td>
      <td>沙县小吃(湘湖地铁站店)</td>
      <td>120.229139</td>
      <td>30.169501</td>
      <td>萧山区</td>
      <td>12.00</td>
      <td>3.5</td>
      <td>餐饮服务;快餐厅;快餐厅</td>
    </tr>
    <tr>
      <th>11</th>
      <td>B0FFIPRET6</td>
      <td>中国兰州牛肉拉面</td>
      <td>120.229132</td>
      <td>30.169558</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>餐饮服务;中餐厅;清真菜馆</td>
    </tr>
    <tr>
      <th>12</th>
      <td>B0FFIGS3FT</td>
      <td>五芳斋回味餐厅(风情大道店)</td>
      <td>120.229156</td>
      <td>30.169535</td>
      <td>萧山区</td>
      <td>27.00</td>
      <td>3.5</td>
      <td>餐饮服务;中餐厅;中餐厅</td>
    </tr>
    <tr>
      <th>13</th>
      <td>B0GU47VZ5R</td>
      <td>吉祥馄饨(都会艺境店)</td>
      <td>120.228688</td>
      <td>30.170414</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>餐饮服务;快餐厅;快餐厅</td>
    </tr>
    <tr>
      <th>14</th>
      <td>B0FFM5KJR3</td>
      <td>银和设计谷设计师俱乐部</td>
      <td>120.228681</td>
      <td>30.169832</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>公司企业;公司;公司</td>
    </tr>
    <tr>
      <th>15</th>
      <td>B0FFLLCX5C</td>
      <td>怪兽充电(天猫小店)</td>
      <td>120.229043</td>
      <td>30.169480</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;共享设备;充电宝</td>
    </tr>
    <tr>
      <th>16</th>
      <td>B0FFLAULB2</td>
      <td>街电(天猫小店)</td>
      <td>120.229043</td>
      <td>30.169480</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;共享设备;充电宝</td>
    </tr>
    <tr>
      <th>17</th>
      <td>B0FFLE0KBC</td>
      <td>巴比馒头(杭州湘西路店)</td>
      <td>120.228998</td>
      <td>30.169495</td>
      <td>萧山区</td>
      <td>16.00</td>
      <td>4.2</td>
      <td>餐饮服务;餐饮相关场所;餐饮相关</td>
    </tr>
    <tr>
      <th>18</th>
      <td>B0FFF2GIFR</td>
      <td>湘湖地铁站C出入口自行车租赁点</td>
      <td>120.229553</td>
      <td>30.169417</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>19</th>
      <td>B0FFLLRH0A</td>
      <td>怪兽充电(佰佳旺湘湖店)</td>
      <td>120.228866</td>
      <td>30.169468</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;共享设备;充电宝</td>
    </tr>
    <tr>
      <th>20</th>
      <td>B0FFILDDTJ</td>
      <td>佰佳旺(湘湖店)</td>
      <td>120.228866</td>
      <td>30.169468</td>
      <td>萧山区</td>
      <td>27.00</td>
      <td>3.5</td>
      <td>餐饮服务;餐饮相关场所;餐饮相关</td>
    </tr>
    <tr>
      <th>21</th>
      <td>B0FFFX8QDX</td>
      <td>饮约(风情大道)</td>
      <td>120.229468</td>
      <td>30.170975</td>
      <td>萧山区</td>
      <td>8.00</td>
      <td>[]</td>
      <td>餐饮服务;冷饮店;冷饮店</td>
    </tr>
    <tr>
      <th>22</th>
      <td>B0FFF07JOJ</td>
      <td>湘湖地铁站B出入口自行车租赁点</td>
      <td>120.229544</td>
      <td>30.171002</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>3.0</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>23</th>
      <td>B0FFLKYOWT</td>
      <td>怪兽充电(湘湖便利店)</td>
      <td>120.229538</td>
      <td>30.171003</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;共享设备;充电宝</td>
    </tr>
    <tr>
      <th>24</th>
      <td>B0GDCC7OBX</td>
      <td>家香味小火锅</td>
      <td>120.228864</td>
      <td>30.170937</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>3.5</td>
      <td>餐饮服务;中餐厅;火锅店</td>
    </tr>
    <tr>
      <th>25</th>
      <td>B0FFMFHVN3</td>
      <td>金地滨江万科悦虹湾售楼处</td>
      <td>120.228340</td>
      <td>30.170604</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>26</th>
      <td>B0GU679ERS</td>
      <td>张亮麻辣烫(都会艺境店)</td>
      <td>120.228451</td>
      <td>30.170856</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>3.5</td>
      <td>餐饮服务;餐饮相关场所;餐饮相关</td>
    </tr>
    <tr>
      <th>27</th>
      <td>B0GDS5RN37</td>
      <td>衢味鱼庄(湘湖店)</td>
      <td>120.228153</td>
      <td>30.170353</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>餐饮服务;中餐厅;中餐厅</td>
    </tr>
    <tr>
      <th>28</th>
      <td>B0FFLQG5QW</td>
      <td>中国电建风情大道改建工程项目部</td>
      <td>120.230588</td>
      <td>30.169893</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>公司企业;公司;公司</td>
    </tr>
    <tr>
      <th>29</th>
      <td>B0GU97TOQO</td>
      <td>NEOIMAGE易美吉</td>
      <td>120.228271</td>
      <td>30.170694</td>
      <td>萧山区</td>
      <td>86.00</td>
      <td>5.0</td>
      <td>生活服务;美容美发店;美容美发店</td>
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
    <tr>
      <th>73</th>
      <td>B0FFIYHNZ8</td>
      <td>杭州萧山旅游汽车有限公司</td>
      <td>120.234843</td>
      <td>30.168105</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>公司企业;公司;公司</td>
    </tr>
    <tr>
      <th>74</th>
      <td>B0FFK66RDK</td>
      <td>东北水饺(湘湖家园39栋1单元)</td>
      <td>120.232741</td>
      <td>30.174422</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>餐饮服务;餐饮相关场所;餐饮相关</td>
    </tr>
    <tr>
      <th>75</th>
      <td>B0FFF5NFSE</td>
      <td>苏黎士小镇别墅</td>
      <td>120.227485</td>
      <td>30.164791</td>
      <td>萧山区</td>
      <td>34604.00</td>
      <td>[]</td>
      <td>商务住宅;住宅区;住宅小区</td>
    </tr>
    <tr>
      <th>76</th>
      <td>B0GUKUE0LK</td>
      <td>苏黎世小镇</td>
      <td>120.229372</td>
      <td>30.164550</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>商务住宅;住宅区;住宅区</td>
    </tr>
    <tr>
      <th>77</th>
      <td>B0FFLLIL64</td>
      <td>萧山区湖头陈幼儿园</td>
      <td>120.224772</td>
      <td>30.174265</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>科教文化服务;学校;幼儿园</td>
    </tr>
    <tr>
      <th>78</th>
      <td>B0FFHSYZDE</td>
      <td>湖头陈花苑</td>
      <td>120.226995</td>
      <td>30.175528</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>商务住宅;住宅区;住宅小区</td>
    </tr>
    <tr>
      <th>79</th>
      <td>B0FFM8UE5X</td>
      <td>村坊里餐厅</td>
      <td>120.229461</td>
      <td>30.164178</td>
      <td>萧山区</td>
      <td>67.00</td>
      <td>3.5</td>
      <td>餐饮服务;中餐厅;综合酒楼</td>
    </tr>
    <tr>
      <th>80</th>
      <td>B0FFHLN7CO</td>
      <td>浙江耀圣建设有限公司东湘社区城中村改造安置房一期项目</td>
      <td>120.236261</td>
      <td>30.170575</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>商务住宅;住宅区;住宅区</td>
    </tr>
    <tr>
      <th>81</th>
      <td>B0FFJIKL01</td>
      <td>都会意境售楼部</td>
      <td>120.236293</td>
      <td>30.170423</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>82</th>
      <td>B023B0AC23</td>
      <td>湘湖家园</td>
      <td>120.232799</td>
      <td>30.175348</td>
      <td>萧山区</td>
      <td>27754.00</td>
      <td>[]</td>
      <td>商务住宅;住宅区;住宅小区</td>
    </tr>
    <tr>
      <th>83</th>
      <td>B0FFHGDAMX</td>
      <td>杭州尚集贸易有限公司</td>
      <td>120.225289</td>
      <td>30.165165</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>公司企业;公司;公司</td>
    </tr>
    <tr>
      <th>84</th>
      <td>B0FFLB9G0I</td>
      <td>菜鸟驿站(杭州湖头陈花苑西门11-3商铺)</td>
      <td>120.226871</td>
      <td>30.176173</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;物流速递;物流速递</td>
    </tr>
    <tr>
      <th>85</th>
      <td>B0FFLA7Y66</td>
      <td>安时达家电服务中心</td>
      <td>120.230308</td>
      <td>30.176677</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;维修站点;维修站点</td>
    </tr>
    <tr>
      <th>86</th>
      <td>B0FFJO036L</td>
      <td>董泽民诊所</td>
      <td>120.230514</td>
      <td>30.176605</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>医疗保健服务;诊所;诊所</td>
    </tr>
    <tr>
      <th>87</th>
      <td>B0FFJF9G37</td>
      <td>百世邻里</td>
      <td>120.230981</td>
      <td>30.176593</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;物流速递;物流速递</td>
    </tr>
    <tr>
      <th>88</th>
      <td>B023B19PFO</td>
      <td>萧山区湘湖幼儿园</td>
      <td>120.233162</td>
      <td>30.175885</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>科教文化服务;学校;幼儿园</td>
    </tr>
    <tr>
      <th>89</th>
      <td>B0FFL962YX</td>
      <td>菜鸟驿站(杭州市萧山区湘湖家园883号店)</td>
      <td>120.231568</td>
      <td>30.176576</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;物流速递;物流速递</td>
    </tr>
    <tr>
      <th>90</th>
      <td>B0FFLJVWZ4</td>
      <td>杭州办事综合自助终端机（萧山区城厢街道湘湖社区）</td>
      <td>120.232616</td>
      <td>30.176227</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>91</th>
      <td>B0FFK8FON9</td>
      <td>一景乳业萧山第一分公司</td>
      <td>120.231980</td>
      <td>30.176552</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>公司企业;公司;公司</td>
    </tr>
    <tr>
      <th>92</th>
      <td>B0FFF2MEI6</td>
      <td>湘湖社区文化活动中心</td>
      <td>120.232582</td>
      <td>30.176304</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>商务住宅;住宅区;社区中心|科教文化服务;文化宫;文化宫</td>
    </tr>
    <tr>
      <th>93</th>
      <td>B0FFLIQ27E</td>
      <td>好嘞易腐垃圾收集站</td>
      <td>120.233522</td>
      <td>30.176000</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;生活服务场所;生活服务场所</td>
    </tr>
    <tr>
      <th>94</th>
      <td>B023B0BPQY</td>
      <td>湘湖社区卫生服务站</td>
      <td>120.232555</td>
      <td>30.176518</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>医疗保健服务;综合医院;卫生院</td>
    </tr>
    <tr>
      <th>95</th>
      <td>B0FFMGPHDY</td>
      <td>萧山区城厢街道社区卫生服务中心</td>
      <td>120.232457</td>
      <td>30.176534</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>医疗保健服务;综合医院;卫生院</td>
    </tr>
    <tr>
      <th>96</th>
      <td>B023B0BPQS</td>
      <td>湘湖农家土菜馆(萧西路店)</td>
      <td>120.231587</td>
      <td>30.177015</td>
      <td>萧山区</td>
      <td>71.00</td>
      <td>3.0</td>
      <td>餐饮服务;中餐厅;中餐厅</td>
    </tr>
    <tr>
      <th>97</th>
      <td>B0GRD9KLVV</td>
      <td>阿芳理发</td>
      <td>120.231691</td>
      <td>30.177015</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;美容美发店;美容美发店</td>
    </tr>
    <tr>
      <th>98</th>
      <td>B0FFJRSKZD</td>
      <td>阿芳理发</td>
      <td>120.231812</td>
      <td>30.176999</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>生活服务;美容美发店;美容美发店</td>
    </tr>
    <tr>
      <th>99</th>
      <td>B0FFIVGYV4</td>
      <td>高盛龙涤物业管理集团有限公司</td>
      <td>120.233160</td>
      <td>30.176524</td>
      <td>萧山区</td>
      <td>[]</td>
      <td>[]</td>
      <td>公司企业;公司;公司</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 8 columns</p>
</div>



### 定制自己的POI请求程序


```python
type_list=['050000','060000','070000']
```


```python
for i,typei in enumerate(type_list):
    print(i,typei)
    URL_i=http+key+para_loc+typei+'&output=json&offset=25&extensions=all&page='
    pois_i=amaPoi.getpois(URL_i)                                                           

    filePath_i = 'E:/zixunHUANG/2019-2021_Project/202007_FridaySalon/week200724/'+str(i).zfill(2)+'.csv'
    amaPoi.write_to_csv(pois_i,filePath_i)                                                 
    print('Done!!!')
```

    0 050000
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    Scraping...
    
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-10-376b7908c9e5> in <module>()
          2     print(i,typei)
          3     URL_i=http+key+para_loc+typei+'&output=json&offset=25&extensions=all&page='
    ----> 4     pois_i=amaPoi.getpois(URL_i)
          5 
          6     filePath_i = 'E:/zixunHUANG/2019-2021_Project/202007_FridaySalon/week200724/'+str(i).zfill(2)+'.csv'
    

    E:\zixunHUANG\2019-2021_Project\202007_FridaySalon\week200724\amaPoi.py in getpois(poi_search_url)
         30     poilist = []
         31     while True:
    ---> 32         result = getpoi_page(poi_search_url, i)
         33         print('Scraping...\n')
         34         result = json.loads(result)
    

    E:\zixunHUANG\2019-2021_Project\202007_FridaySalon\week200724\amaPoi.py in getpoi_page(poi_search_url, page)
         18     req_url = 'http://'+poi_search_url+str(page)
         19     data = ''
    ---> 20     with request.urlopen(req_url) as f:
         21         data = f.read()
         22         data = data.decode('utf-8')
    

    ~\Anaconda3\lib\urllib\request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        221     else:
        222         opener = _opener
    --> 223     return opener.open(url, data, timeout)
        224 
        225 def install_opener(opener):
    

    ~\Anaconda3\lib\urllib\request.py in open(self, fullurl, data, timeout)
        524             req = meth(req)
        525 
    --> 526         response = self._open(req, data)
        527 
        528         # post-process response
    

    ~\Anaconda3\lib\urllib\request.py in _open(self, req, data)
        542         protocol = req.type
        543         result = self._call_chain(self.handle_open, protocol, protocol +
    --> 544                                   '_open', req)
        545         if result:
        546             return result
    

    ~\Anaconda3\lib\urllib\request.py in _call_chain(self, chain, kind, meth_name, *args)
        502         for handler in handlers:
        503             func = getattr(handler, meth_name)
    --> 504             result = func(*args)
        505             if result is not None:
        506                 return result
    

    ~\Anaconda3\lib\urllib\request.py in http_open(self, req)
       1344 
       1345     def http_open(self, req):
    -> 1346         return self.do_open(http.client.HTTPConnection, req)
       1347 
       1348     http_request = AbstractHTTPHandler.do_request_
    

    ~\Anaconda3\lib\urllib\request.py in do_open(self, http_class, req, **http_conn_args)
       1319             except OSError as err: # timeout error
       1320                 raise URLError(err)
    -> 1321             r = h.getresponse()
       1322         except:
       1323             h.close()
    

    ~\Anaconda3\lib\http\client.py in getresponse(self)
       1329         try:
       1330             try:
    -> 1331                 response.begin()
       1332             except ConnectionError:
       1333                 self.close()
    

    ~\Anaconda3\lib\http\client.py in begin(self)
        295         # read until we get a non-100 response
        296         while True:
    --> 297             version, status, reason = self._read_status()
        298             if status != CONTINUE:
        299                 break
    

    ~\Anaconda3\lib\http\client.py in _read_status(self)
        256 
        257     def _read_status(self):
    --> 258         line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
        259         if len(line) > _MAXLINE:
        260             raise LineTooLong("status line")
    

    ~\Anaconda3\lib\socket.py in readinto(self, b)
        584         while True:
        585             try:
    --> 586                 return self._sock.recv_into(b)
        587             except timeout:
        588                 self._timeout_occurred = True
    

    KeyboardInterrupt: 



```python

```

---
**Email:** huangzxarchitecture@zju.edu.cn
