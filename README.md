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
---
**Email:** huangzxarchitecture@zju.edu.cn
