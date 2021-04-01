# DAMN_Data_Toolkit
### Brief Intro
The third-party package is currently divided into two parts, one part is used for obtaining urban big data such as points of interest, area of interest, social media data with geo-information, and the other part is used for extracting geographic distribution features to help designers visualize mass urban information.
### Installation
```python
python setup.py install
```
---
### Damn GeoSpider
- [x] GeoAutoNavi
- [ ] GeoSocialMedia
### Damn GeoBee
- [x] GeoKit
- [x] HotGrid
- [ ] GeoHash
### How to Use it
* **example 1**
```python
import pandas as pd
chengdu_poi = pd.read_csv('chengdu_poi.csv').drop(columns='Unnamed: 0')
chengdu_poi.tail(1)
```
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

* **example 2**
```python
hg = HotGridGenerator(gridUnit = 1000,searchRadius = 1000)
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
![example](https://user-images.githubusercontent.com/39406532/113274208-00604100-9310-11eb-9ae4-60f5a499fded.png)
---
**Email:** huangzxarchitecture@zju.edu.cn
