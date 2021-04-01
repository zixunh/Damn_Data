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
### Examples
```python
import pandas as pd
chengdu_poi = pd.read_csv('chengdu_poi.csv').drop(columns='Unnamed: 0')
chengdu_poi.tail(1)
```
```python
from damndata.damn_geoBee.hotgrid import HotGridGenerator
hg = HotGridGenerator(gridUnit = 1000,searchRadius = 1000)
hg.grid_setting(chengdu_poi,'wgslat','wgslng')
chengdu_poi_hotMap=hg.gridCounting_basic(chengdu_poi,'wgslat','wgslng')
```
```python
import seaborn as sns
from IPython.core.pylabtools import figsize
figsize(21,12)
sns.heatmap(chengdu_poi_hotMap.sort_index(axis=0,ascending=False))
```
---
**Email:** huangzxarchitecture@zju.edu.cn
